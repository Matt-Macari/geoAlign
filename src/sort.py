###################################################################################
# Developed by Matthew Marcotullio, Matt Macari, Lily Yassemi, and Dylan Lucas    #
#             for California Polytechnic State University, Humboldt               #
###################################################################################
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
from  matplotlib.patches import Polygon as MplPolygon
import numpy as np


def sort_keypoints_by_section(width, height, query_keypoints, train_keypoints):
    ignore_borders = True

    if ignore_borders:
        upper_scale = 0.1
        side_scale = 0.04
        bottom_scale = 0.04
        side_margin_x = width * side_scale
        upper_margin_y = height * upper_scale
        bottom_margin_y = height * bottom_scale

        x_coords = (width - (side_margin_x * 2)) / 3
        y_coords = (height - (upper_margin_y + bottom_margin_y) / 3)


        X0 = 0 
        X1 = X0 + side_margin_x
        X2 = X1 + 1
        X3 = X2 + x_coords
        X4 = X3 + 1
        X5 = X4 + x_coords
        X6 = X5 + 1
        X7 = X6 + x_coords
        X8 = X7 + 1
        X9 = X8 + 1
        X10 = width 

        Y0 = 0
        Y1 = Y0 + upper_margin_y
        Y2 = Y1 + 1
        Y3 = Y2 + y_coords
        Y4 = Y3 + 1
        Y5 = Y4 + y_coords
        Y6 = Y5 + 1
        Y7 = Y6 + y_coords
        Y8 = Y7 + 1
        Y9 = Y8 + bottom_margin_y

        #define polygons:
        out_of_bounds_upper = Polygon([(X0, Y0), (X10, Y0), (X10, Y1), (X0, Y1)])
        out_of_bounds_left = Polygon([(X0, Y2), (X1, Y2), (X1, Y9), (X0, Y9)])
        out_of_bounds_right = Polygon([(X9, Y2), (X10, Y2), (X10, Y9), (X9, Y9)])
        out_of_bounds_bottom = Polygon([(X2, Y8), (X8, Y8), (X8, Y9), (X2, Y9)])
        polygon1 = Polygon([(X2, Y2), (X3, Y2), (X3, Y3), (X2, Y3)])
        polygon2 = Polygon([(X4, Y2), (X5, Y2), (X5, Y3), (X4, Y3)])
        polygon3 = Polygon([(X6, Y2), (X7, Y2), (X7, Y3), (X6, Y3)])
        polygon4 = Polygon([(X2, Y4), (X3, Y4), (X3, Y5), (X2, Y5)])
        polygon5 = Polygon([(X4, Y4), (X5, Y4), (X5, Y5), (X4, Y5)])
        polygon6 = Polygon([(X6, Y4), (X7, Y4), (X7, Y5), (X6, Y5)])
        polygon7 = Polygon([(X2, Y6), (X3, Y6), (X3, Y7), (X2, Y7)])
        polygon8 = Polygon([(X4, Y6), (X5, Y6), (X5, Y7), (X4, Y7)])
        polygon9 = Polygon([(X6, Y6), (X7, Y6), (X7, Y7), (X6, Y7)])

        polygons = [out_of_bounds_upper, out_of_bounds_left, out_of_bounds_right, out_of_bounds_bottom, \
                    polygon1, polygon2, polygon3, polygon4, polygon5, polygon6, polygon7, polygon8, polygon9]

        # Extract the keypoints and convert them into Shapely Points
        query_keypoints_points = [Point(kp) for kp in query_keypoints]
        train_keypoints_points = [Point(kp) for kp in train_keypoints]

        # print(f'\n\n\nquery_keypoints_points ({len(query_keypoints_points)}): {query_keypoints_points}\n\n\n')
        # print(f'\n\n\ntrain_keypoints_points ({len(train_keypoints_points)}): {train_keypoints_points}\n\n\n')

        # Combine the matching Points into a two-dimensional array
        matching_points_array = np.array([[query_pt, train_pt] for query_pt, train_pt in zip(query_keypoints_points, train_keypoints_points)])

        #print(f'\n\n\nmatching_points_array: {matching_points_array}\n\n\n')
        matching_keypoints_upper = []
        matching_keypoints_left = []
        matching_keypoints_right = []
        matching_keypoints_bottom = []
        matching_keypoints_sect1 = []
        matching_keypoints_sect2 = []
        matching_keypoints_sect3 = []
        matching_keypoints_sect4 = []
        matching_keypoints_sect5 = []
        matching_keypoints_sect6 = []
        matching_keypoints_sect7 = []
        matching_keypoints_sect8 = []
        matching_keypoints_sect9 = []

        sections = [matching_keypoints_upper, matching_keypoints_left, \
                    matching_keypoints_right, matching_keypoints_bottom, \
                    matching_keypoints_sect1, matching_keypoints_sect2, \
                    matching_keypoints_sect3, matching_keypoints_sect4, \
                    matching_keypoints_sect5, matching_keypoints_sect6, \
                    matching_keypoints_sect7, matching_keypoints_sect8, \
                    matching_keypoints_sect9]
        
        for match in matching_points_array:
            query_point, train_point = match
            for i, polygon in enumerate(polygons): 
                if polygon.contains(query_point):
                    sections[i].append([query_point, train_point])


    else:
        x_coords = width / 3 
        y_coords = height / 3

        # constants
        Y1 = 0
        Y2 = y_coords - 1
        Y3 = y_coords
        Y4 = (y_coords * 2) - 1
        Y5 = y_coords * 2
        Y6 = y_coords * 3

        X1 = 0
        X2 = x_coords - 1
        X3 = x_coords
        X4 = (x_coords * 2) - 1
        X5 = x_coords * 2
        X6 = x_coords * 3

        #define polygons
        polygon1 = Polygon([(X1,Y1), (X2, Y1), (X2, Y2), (X1, Y2)])

        polygon2 = Polygon([(X3,Y1), (X4, Y1), (X4, Y2), (X3, Y2)])

        polygon3 = Polygon([(X5,Y1), (X6, Y1), (X6,Y2), (X5,Y2)])

        polygon4 = Polygon([(X1,Y3), (X2, Y3), (X2, Y4), (X1, Y4)])

        polygon5 = Polygon([(X3,Y3), (X4, Y3), (X4,Y4), (X3, Y4)])

        polygon6 = Polygon([(X5,Y3), (X6,Y3), (X6,Y4), (X5,Y4)])

        polygon7 = Polygon([(X1,Y5), (X2,Y5), (X2, Y6), (X1,Y6)])

        polygon8 = Polygon([(X3,Y5), (X4, Y5),(X4, Y6), (X3, Y6)])

        polygon9 = Polygon([(X5,Y5), (X6,Y5), (X6,Y6), (X5,Y6)])


        polygons = [polygon1, polygon2, polygon3, polygon4, polygon5, polygon6, polygon7, polygon8, polygon9]

        # Extract the keypoints and convert them into Shapely Points
        query_keypoints_points = [Point(kp) for kp in query_keypoints]
        train_keypoints_points = [Point(kp) for kp in train_keypoints]

        # print(f'\n\n\nquery_keypoints_points ({len(query_keypoints_points)}): {query_keypoints_points}\n\n\n')
        # print(f'\n\n\ntrain_keypoints_points ({len(train_keypoints_points)}): {train_keypoints_points}\n\n\n')

        # Combine the matching Points into a two-dimensional array
        matching_points_array = np.array([[query_pt, train_pt] for query_pt, train_pt in zip(query_keypoints_points, train_keypoints_points)])

        #print(f'\n\n\nmatching_points_array: {matching_points_array}\n\n\n')

        matching_keypoints_sect1 = []
        matching_keypoints_sect2 = []
        matching_keypoints_sect3 = []
        matching_keypoints_sect4 = []
        matching_keypoints_sect5 = []
        matching_keypoints_sect6 = []
        matching_keypoints_sect7 = []
        matching_keypoints_sect8 = []
        matching_keypoints_sect9 = []

        sections = [matching_keypoints_sect1, matching_keypoints_sect2, \
                    matching_keypoints_sect3, matching_keypoints_sect4, \
                    matching_keypoints_sect5, matching_keypoints_sect6, \
                    matching_keypoints_sect7, matching_keypoints_sect8, \
                    matching_keypoints_sect9]
        
        for match in matching_points_array:
            query_point, train_point = match
            for i, polygon in enumerate(polygons): 
                if polygon.contains(query_point):
                    sections[i].append([query_point, train_point])


    """
    # ------------------------------------------------------------------------------------------ 
    # ----------------------------STARTING VISUALIZATION CODE ----------------------------------
    #-------------------------------------------------------------------------------------------
    # ------THE FOLLOWING IS JUST TO VISUALIZE THE POLYGONS AND COORESPONDING QUERY POINTS------
    #-------------------------------------------------------------------------------------------

    # Create a single figure and axis for plotting everything together
    fig, ax = plt.subplots()

    # Variables to track min/max coordinates for dynamic scaling
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')

    # Plot all the polygons and their corresponding query points
    for i, each in enumerate(polygons):
        # Extract the exterior coordinates from the Shapely polygon and convert to a numpy array
        polygon_coords = np.array(each.exterior.coords)
        
        # Update the min/max coordinates
        min_x = min(min_x, polygon_coords[:, 0].min())
        max_x = max(max_x, polygon_coords[:, 0].max())
        min_y = min(min_y, polygon_coords[:, 1].min())
        max_y = max(max_y, polygon_coords[:, 1].max())

        # Plot the polygon using matplotlib's Polygon
        ax.add_patch(MplPolygon(polygon_coords, closed=True, edgecolor='blue', fill=None))
        
        # Plot the query points in the corresponding section
        section = sections[i]
        
        for point_pair in section:  # Each point_pair contains [query_point, train_point]
            query_point, _ = point_pair  # Ignore train_point, only plot query_point
            ax.plot(query_point.x, query_point.y, 'ro')  # Red circle for query points

            # Update the min/max coordinates for query points
            min_x = min(min_x, query_point.x)
            max_x = max(max_x, query_point.x)
            min_y = min(min_y, query_point.y)
            max_y = max(max_y, query_point.y)

        # Add a label to the polygon at its centroid
        centroid = each.centroid

        if i == 0: ax.text(centroid.x, centroid.y, f'Upper OB', color='black', fontsize=12, ha='center', va='center')
        elif i== 1: ax.text(centroid.x, centroid.y, f'Left OB', color='black', fontsize=12, ha='center', va='center')
        elif i == 2: ax.text(centroid.x, centroid.y, f'Right OB', color='black', fontsize=12, ha='center', va='center')
        elif i == 3: ax.text(centroid.x, centroid.y, f'Bottom OB', color='black', fontsize=12, ha='center', va='center')
        else:
            ax.text(centroid.x, centroid.y, f'Polygon {i-3}', color='black', fontsize=12, ha='center', va='center')

    # Add a small padding to the limits
    padding = 50  # Adjust padding as needed
    ax.set_xlim(min_x - padding, max_x + padding)
    ax.set_ylim(max_y + padding, min_y - padding)  # Inverted y-axis

    # Enable the grid
    plt.grid(True)

    # Display the final combined plot
    plt.show()

    # ------------------------------------------------------------------------------------------ 
    # ------------------------------------------------------------------------------------------
    #-----------------------------ENDING VISUALIZATION CODE-------------------------------------
    # ------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------
    """




    #polygons does not need to be returned, except for visualization code in main
    #   when visualization is no longer necessary, modify to only return sections
    return sections, polygons
