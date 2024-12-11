###################################################################################
# Developed by Matthew Marcotullio, Matt Macari, Lily Yassemi, and Dylan Lucas    #
#             for California Polytechnic State University, Humboldt               #
###################################################################################
import os

# From the terminal, prompts user to input a path
# Prints properties of the path user inputs
# Returns the path the user inputs
# Returns "exit" if the selection is canceled
def get_input_path():
    while True:
        path = input("\nPlease enter the path to a directory: \nType 'Exit' to cancel\n").strip()

        if path.lower() == 'exit':
            print("Exiting the program.")
            return "exit", 0
        
        if not os.path.isdir(path):
            print("\nThe path is not a valid directory. Please try again.\n")
            continue

        files = [f for f in os.listdir(path) if not f.startswith('.')]

        if not files:
            print("\nThe selected folder is empty. Please enter a path to a folder with files.\n")
            continue

        print(f"\nFolder selected: {path}\n")

        tif_files = []
        other_files = []
        total_tif_size = 0

        for filename in files:
            full_path = os.path.join(path, filename)

            if os.path.isfile(full_path):
                if filename.lower().endswith(('.tif', '.tiff')):
                    tif_files.append(filename)
                    total_tif_size += os.path.getsize(full_path)
                elif filename != '.DS_Store':
                    other_files.append(filename)

        num_tif_files = len(tif_files)

        if num_tif_files > 0:
            print('Input directory statistics:')
            print(f"Number of TIFF files: {num_tif_files}")

            # Check if size is 1 GB or more and display accordingly
            total_size_gb = total_tif_size / (1024 * 1024 * 1024)
            if total_size_gb >= 1:
                print(f"Total size of all TIFF files: {total_size_gb:.2f} GB")
            else:
                total_size_mb = total_tif_size / (1024 * 1024)
                print(f"Total size of all TIFF files: {total_size_mb:.2f} MB")

            if len(other_files) > 0:
                print(f"Number of non-TIFF files found: {len(other_files)}")
            return path, num_tif_files
        else:
            print("No TIFF files found in the selected folder. Please select a different folder.\n")

# From the terminal, prompts user to input a path
# Returns the path the user inputs
# Returns "exit" if the selection is canceled
def get_output_path():
    while True:
        path = input("\nPlease enter the path to a directory to save geo-referenced files to: \nType 'Exit' to cancel\n").strip()

        if path.lower() == 'exit':
            print("Exiting the program.")
            return "exit"

        if not os.path.isdir(path):
            print("\nThe output path is not a valid directory. Please try again.")
        else:
            print(f"\nFolder selected: {path}\n")
            return path