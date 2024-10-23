# import sys  # To flush the output immediately
# import time
from tkinter.filedialog import askdirectory
import tkinter as tk
import os
os.environ['PYTHONWARNINGS'] = 'ignore::UserWarning'
os.environ['NO_IMK_CLIENT'] = '1'  # Disables IMKClient messages


# Hide the Tkinter root window
root = tk.Tk()
root.withdraw()

# prints properties of folder user selects
# Returns path for folder user selects
# Returns "exit" if selection is cancled
def get_input_path():
    while True:
        # Step 1: Ask user to select the first folder (input folder)
        path = askdirectory(title='Select a folder')

        if path:
            print(f"\nFolder selected: {path}\n")

            tif_files = []
            other_files = []
            total_tif_size = 0

            for filename in os.listdir(path):
                full_path = os.path.join(path, filename)

                if os.path.isfile(full_path):
                    if filename.lower().endswith(('.tif', '.tiff')):
                        tif_files.append(filename)
                        total_tif_size += os.path.getsize(full_path)
                    else:
                        other_files.append(filename)

            if len(tif_files) > 0:
                print(f"Number of TIF files found: {len(tif_files)}")

                # Check if size is 1 GB or more and display accordingly
                total_size_gb = total_tif_size / (1024 * 1024 * 1024)
                if total_size_gb >= 1:
                    print(f"Total size of TIF files: {total_size_gb:.2f} GB")
                else:
                    total_size_mb = total_tif_size / (1024 * 1024)
                    print(f"Total size of TIF files: {total_size_mb:.2f} MB")
                
                print(f"Number of non-TIF files found: {len(other_files)}")
                return path  # Only return if TIF files are found
            else:
                print("No TIF files found in the selected folder. Please select a different folder.")
        else:
            print("No folder selected. Exiting the program.")
            return "exit"

# Returns path for folder user selects
# Returns "exit" if selection is cancled
def get_output_path():
    while True:
            # Step 2: Ask user to select the second folder (output folder)
            print()
            path = askdirectory(
                title='Select a folder to save geo referenced files to')
            if path:
                # Step 3: Loop through each TIFF file and create a text file in the output directory
                print(f"\n Return folder selected: {path}\n")
                return path
            else:
                print("No folder selected. Exiting the program.")
                return "exit"
            
# Depricated code for time being
# Use for later when we write the code to loop through each file in main
# Loop through each TIFF file and create a text file in the output directory
"""
                print(f"\n Return folder selected: {path}\n")
                for idx, tif_file in enumerate(tif_files, 1):
                    # Print progress in the same line using carriage return
                    print(f"\rProcessing file {idx} of {
                          len(tif_files)}: {tif_file}", end="")

                    # Flush the output buffer to force print the line in real-time
                    sys.stdout.flush()

                    # Pause for 1 seconds
                    time.sleep(1)

                    # Construct the text file name based on the TIFF file name
                    text_filename = f"{os.path.splitext(tif_file)[0]}.txt"
                    text_file_path = os.path.join(output_dir, text_filename)

                    # Create the text file and write "hello world" in it
                    with open(text_file_path, 'w') as f:
                        f.write("hello world")

                # Move to a new line after the last file is processed
                print("\nAll text files created successfully.")
"""