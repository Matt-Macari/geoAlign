###################################################################################
# Developed by Matthew Marcotullio, Matt Macari, Lily Yassemi, and Dylan Lucas    #
#             for California Polytechnic State University, Humboldt               #
###################################################################################
import orb as orb
import sort as sort
import trim as trim
import matplotlib.pyplot as plt
from  matplotlib.patches import Polygon as MplPolygon
import numpy as np
import folder_prompt as folder_prompt
import path_prompt as path_prompt
import georef as gf
import os
import time
import sys



def main():

    train_image_path = 'data/demo_base.tif'

    # Prompt user to select an input folder
    input_dir, num_tiff_files = folder_prompt.select_input_folder()
    if input_dir == "exit":
        sys.exit()

    # Prompt user to select an output folder
    output_dir = folder_prompt.select_output_folder()

    if output_dir == "exit":
        sys.exit()

    num_files_processed = 0
    num_files_failed = 0
    failed_files = []

    # loop through each .tif in given directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".tif"):
            curr_file = os.path.join(input_dir, filename)
            # set output path (output_dir + current file being processed, with _out appended)
            base, ext = os.path.splitext(os.path.basename(curr_file))
            out_path = output_dir + '/' + f"{base}_out{ext}"

            # find keypoints with orb algorithm: 
            train_image_width, train_image_height, sorted_matches, \
            query_keypoints, train_keypoints = orb.orb_detect(train_image_path, curr_file)
    
            # note: after sorting, some lists may be empty
            # can remove polygons, this is only for the visualization below (remove polygons 
            #       from being returned in sort_keypoints_by_section)
            sections_list, polygons = sort.sort_keypoints_by_section(train_image_width, train_image_height, \
                                        query_keypoints, train_keypoints)
    
            # trim the lists:
            # trimmed_sections_list is only used for the visualization below, 
            #   flattened_trimmed_sections_list is used for georeference() call
            trimmed_sections_list, flattened_trimmed_sections_list = trim.trim_sections(sections_list)

            # if no keypoints are found, print error and skip georeference call
            if not flattened_trimmed_sections_list or all(not row for row in flattened_trimmed_sections_list):
                print(f'\nERROR: No keypoints found in {curr_file}... Continuing processing with the next image')
                num_files_processed += 1
                num_files_failed += 1
                failed_files.append(curr_file)
                continue

            # georeference 
            gf.georeference(flattened_trimmed_sections_list, train_image_path, curr_file, out_path)
            num_files_processed += 1

            print(f'\rProcessing file {num_files_processed} out of {num_tiff_files}', end='', flush=True)
    print('\n\n-----------------------')
    print('\nFiles have been processed...')
    print(f'\nNumber of files successfully georeferenced: {num_files_processed - num_files_failed}')
    print(f'\nNumber of failed files: {num_files_failed}')
    if failed_files:
        print('\nFiles that failed during processing:\n')
        for each in failed_files:
            print(f'{each}\n')
    print('------------------------------------------------------------------------')
    print(f'Check {output_dir} for the results.')

"""
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
if __name__ == "__main__":
    main()
