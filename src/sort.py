import orb as orb
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
from  matplotlib.patches import Polygon as MplPolygon
import numpy as np


def sort_keypoints_by_section(width, height, sorted_matches, query_keypoints, train_keypoints):
    xCords = width / 3 
    yCords = height / 3

    # constants
    Y1 = 0
    Y2 = yCords - 1
    Y3 = yCords
    Y4 = (yCords * 2) - 1
    Y5 = yCords * 2
    Y6 = yCords * 3

    X1 = 0
    X2 = xCords - 1
    X3 = xCords
    X4 = (xCords * 2) - 1
    X5 = xCords * 2
    X6 = xCords * 3

    #define polygon 1
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
    query_keypoints_points = [Point(query_keypoints[m.queryIdx]) for m in sorted_matches if m.queryIdx < len(query_keypoints)]
    train_keypoints_points = [Point(train_keypoints[m.trainIdx]) for m in sorted_matches if m.trainIdx < len(train_keypoints)]
    
    # Combine the matching Points into a two-dimensional array
    matching_points_array = np.array([[query_pt, train_pt] for query_pt, train_pt in zip(query_keypoints_points, train_keypoints_points)])

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
        ax.text(centroid.x, centroid.y, f'Polygon {i+1}', color='black', fontsize=12, ha='center', va='center')

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

    return sections
