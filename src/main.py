import orb as orb
import sort as sort
import trim as trim
import matplotlib.pyplot as plt
from  matplotlib.patches import Polygon as MplPolygon
import numpy as np
import folder_prompt as folder_prompt
import path_prompt as path_prompt


def main():

    # Have user select a folder
    # folder_prompt.select_input_folder()
    # folder_prompt.select_output_folder()

    # Prompt user through the terminal for path
    # path_prompt.get_input_path()
    # path_prompt.get_output_path()

    
    train_image_path = 'data/airPort.jpg'
    query_image_path = 'data/airportCrop.png'

    train_image_width, train_image_height, sorted_matches, \
    query_keypoints, train_keypoints = orb.orb_detect(train_image_path, query_image_path)

    # note: after sorting, some lists may be empty
    # can remove polygons, this is only for the visualization below (remove polygons 
    #       from being returned in sort_keypoints_by_section)
    sections_list, polygons = sort.sort_keypoints_by_section(train_image_width, train_image_height, \
                                   sorted_matches, query_keypoints, \
                                   train_keypoints)
    
    # print('\n\n-----------\n\n -----------\n\n------------\n\n sections list (untrimmed:)\n\n')
    # for i, each in enumerate(sections_list):
    #     print(f'Section {i}: {sections_list[i]} \n\n')
    # print('\n\n-----------\n\n -----------\n\n------------\n\n')
    
    # after this call, each list in sections_list should be trimmed:
    trimmed_sections_list = trim.trim_sections(sections_list)




    # ------------------------------------------------------------------------------------------ 
    # ----------------------------STARTING VISUALIZATION CODE ----------------------------------
    #-------------------------------------------------------------------------------------------
    #----THE FOLLOWING IS JUST TO VISUALIZE THE POLYGONS AND COORESPONDING QUERY POINTS AFTER TRIMMING----
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
        section = trimmed_sections_list[i]
        
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



if __name__ == "__main__":
    main()
