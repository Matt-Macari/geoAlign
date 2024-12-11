###################################################################################
# Developed by Matthew Marcotullio, Matt Macari, Lily Yassemi, and Dylan Lucas    #
#             for California Polytechnic State University, Humboldt               #
###################################################################################
from osgeo import gdal, osr
from shapely.geometry import Point
import random
import os
import csv

# Suppress all GDAL warnings
gdal.PushErrorHandler('CPLQuietErrorHandler')
gdal.DontUseExceptions()

# Expects an image path, turns it into a GDALDataset, 
#   then returns a geotransform of that image

# from gdal.org:
#   - A a GDALDataset contains a list of raster bands, all pertaining 
#       to the same area, and having the same resolution. It also has metadata, 
#       a coordinate system, a georeferencing transform, size of raster and various other information.

#   - A geotransform is an affine transformation from the image coordinate space (row, column), 
#        also known as (pixel, line) to the georeferenced coordinate space (projected or geographic coordinates).

#   - A geotransform consists in a set of 6 coefficients:

#       GT(0) x-coordinate of the upper-left corner of the upper-left pixel.
#       GT(1) w-e pixel resolution / pixel width.
#       GT(2) row rotation (typically zero).
#       GT(3) y-coordinate of the upper-left corner of the upper-left pixel.
#       GT(4) column rotation (typically zero).
#       GT(5) n-s pixel resolution / pixel height (negative value for a north-up image).
def image_to_geotransform(image_path):
    # Load the image to get its geotransform
    image_ds = gdal.Open(image_path)
    geotransform = image_ds.GetGeoTransform()
    return geotransform

# Expects a geotransform, an x pixel and y pixel, and returns the real geographic
#   coordinate of those pixels 
#       X = GT(0) + x * GT(1) + y * GT(2)
#       Y GT(3) + x * GT(4) + y * GT(5)
def pixel_to_geo_coords(geotransform, px, py):
    origin_x, pixel_width, _, origin_y, _, pixel_height = geotransform
    geo_x = origin_x + px * pixel_width
    geo_y = origin_y + py * pixel_height

    # print(f'Longitude (x): {geo_x}')
    # print(f'Latitude (y): {geo_y}')

    return geo_x, geo_y

# Expects a 2-d list of keypoints (matching control points between query and train image), a train
#   image path, a query image path, and an output image path (directory must already exist, image may not)
# Returns nothing, has the side effect of writing a NEW train file as a georeferenced image based on given keypoints
def georeference(keypoints, train_image_path, query_image_path, output_image_path):

    # Load the train image and get its geotransform
    train_geotransform = image_to_geotransform(train_image_path)

    # Load the query image into a GDALDataset
    # from gdal.org: GDALOpen() open(s) a dataset, passing the name of the dataset and the access desired (GA_ReadOnly or GA_Update).
    query_ds = gdal.Open(query_image_path, gdal.GA_ReadOnly)

    # We don't want to modify the user's image, but rather make a copy and modify that one
    # from gdal.org: 
    #   In general new formats are added to GDAL by implementing format specific drivers as subclasses of GDALDataset, 
    #       and band accessors as subclasses of GDALRasterBand. As well, a GDALDriver instance is created for the format, 
    #       and registered with the GDALDriverManager, to ensure that the system knows about the format.
    driver = gdal.GetDriverByName("GTiff")
    # CreateCopy is a driver method
    # From gdal.org: 
    #   CreateCopy​(java.lang.String name, Dataset src_ds, int strict) - Create a copy of a dataset
    # Note: 
    #       - strict=0 allows GDAL to proceed even if the output format doesn’t support all features of the input 
    #           dataset (not an issue for geoTIFFs, but good to include anyway(?))
    #       - a resulting GDALDataset from CreateCopy is writable by default
    #       - IMPORTANT: GDAL will create the specified file path (output_image_path) if it doesn't already
    #           exist, HOWEVER, the directory in which you are saving it must already exist (GDAL doesn't create intermediate dirs)
    out_ds = driver.CreateCopy(output_image_path, query_ds, strict=0)

    # Set up GCP list
    gcps = []
    for query_point, train_point in keypoints:

        # Extract query image pixel coordinates
        # Shapely Point objects store 2D or 3D coordinates, which can be accessed directly as attributes x and y.
        query_x, query_y = query_point.x, query_point.y
        
        # Convert train image pixel coordinates to geographic coordinates
        train_px, train_py = train_point.x, train_point.y
        train_geo_x, train_geo_y = pixel_to_geo_coords(train_geotransform, train_px, train_py)
        
        # Create a GCP
        # GCP contstructor from gdal.org: 
        #       GCP​(double x, double y, double pixel, double line)
        # Note: 
        #       - x is The real-world x-coordinate of the GCP (longitude)
        #       - y is The real-world y-coordinate of the GCP (latitude)
        #       - pixel is the x-coordinate of the GCP in image (pixel) coordinates, representing the column number
        #       - line is the y-coordinate of the GCP in image (pixel) coordinates, representing the row number
        #       - 0 is elevation - implement later? is it in the geoTIFF?
        gcp = gdal.GCP(train_geo_x, train_geo_y, 0, query_x, query_y)
        gcps.append(gcp)

    # Define the spatial reference we want to use:
    # Create a SpatialReference object
    # From gdal.org: This class represents an OpenGIS Spatial Reference System, 
    #   and contains methods for converting between this object organization and well 
    #   known text (WKT) format. This object is reference counted as one instance of the 
    #   object is normally shared between many Geometry objects
    srs = osr.SpatialReference()

    # EPSG:26910 cooresponds to NAD83 / UTM zone 10N (this is the spatial reference we want to use, according to Jim Graham)
    # from spatialreference.org: 
    #   Type: PROJECTED_CRS
    #   WGS84 Bounds: -126.0, 30.54, -119.99, 81.8
    #   Scope: Engineering survey, topographic mapping.
    #   Area: North America - between 126°W and 120°W - onshore and offshore. Canada - 
    #           British Columbia; Northwest Territories; Yukon. United States (USA) - California; Oregon; Washington.
    #   Projection method name: Transverse Mercator
    #   Axes: Easting, Northing (E,N). Directions: east, north. UoM: metre.
    #   Base CRS: EPSG:4269

    # ImportFromEPSG is a SpatialReference method
    # from gdal.org:
    #   importFromEPSGA (int) - Initialize SRS based on EPSG geographic, projected or vertical CRS code.  
    srs.ImportFromEPSG(26910)

    # GDAL requires the spatial reference to be in WKT (Well-Known-Text) format
    # ExportToWkt is a SpatialReference method
    # From gdal.org: 
    #    exportToWkt (char **) const - Convert this SRS into WKT 1 format.
    # Note:
    #      # Note: 
    #       - In GDAL's python bindings, passing the char is not necessary (no need to dynamically allocate mem in python :))
    wkt_projection = srs.ExportToWkt()

    # shuffle list to randomize order of GCPs
    random.shuffle(gcps)

    # Add the GCPs to the query image
    # From gdal.org: 
    #       SetGCPs (int nGCPCount, const GDAL_GCP *pasGCPList, const OGRSpatialReference *poGCP_SRS) - Assign GCPs.
    # Note: 
    #       - In GDAL's python bindings, passing nGCPCount is not necessary (again, no need to dynamically allocate mem in python)
    out_ds.SetGCPs(gcps, wkt_projection)

    '''
    csv_out_path = f'{os.path.dirname(output_image_path)}/{os.path.splitext(os.path.basename(query_image_path))[0]}_GCPs.csv'
    with open(csv_out_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Latitude", "Longitude"])
        
        # Write each GCP's coordinates
        for i, gcp in enumerate(gcps):
            writer.writerow([gcp.GCPY, gcp.GCPX])
    '''
   
    # Define the CSV file name
    csv_out_path = f'{os.path.dirname(output_image_path)}/{os.path.splitext(os.path.basename(query_image_path))[0]}_GCPs.csv'


    source_srs = osr.SpatialReference()
    source_srs.ImportFromEPSG(26910)  # EPSG code for NAD83 / UTM zone 10N

    target_srs = osr.SpatialReference()
    target_srs.ImportFromEPSG(4326)  # EPSG code for WGS84

    transform = osr.CoordinateTransformation(source_srs, target_srs)

    # Write the geographic coordinates to the CSV file
    with open(csv_out_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Latitude", "Longitude"])
        
        for i, gcp in enumerate(gcps):
            # Transform coordinates to geographic system
            lon, lat, _ = transform.TransformPoint(gcp.GCPX, gcp.GCPY)
            writer.writerow([lon, lat])



    # Close the datasets (this "commits" the changes, embedding the GCPs into the image metadata)
    # train_ds = None
    out_ds = None
    query_ds = None

    #print(f'\n\n **************SUCCESS************** \n\n New georeferenced tiff has been written to: {output_image_path}\n\n')

