import os

# From the teminal prompts user to input a path
# prints properties of path user inputs
# Returns path the user inputs
# Returns "exit" if selection is cancled
def get_input_path():
    while True:
        path = input("Please enter the path to a directory: \nType 'Exit' to cancel\n").strip()

        if path.lower() == 'exit':
            print("Exiting the program.")
            return "exit"

        if not os.path.isdir(path):
            print("\nThe path is not a valid directory. Please try again.")
            continue

        files = os.listdir(path)
        print(f"\nFolder selected: {path}")
        print()

        tif_files = []
        other_files = []
        total_tif_size = 0

        for filename in files:
            full_path = os.path.join(path, filename)

            if os.path.isfile(full_path):
                if filename.lower().endswith(('.tif', '.tiff')):
                    tif_files.append(filename)
                    total_tif_size += os.path.getsize(full_path)
                elif (filename != '.DS_Store'):
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
        else:
            print("\nNo TIF files found. Please select a folder with TIF files.")
            continue

        if len(other_files) > 0:
            print(f"Number of non-TIF files found: {len(other_files)}")
            print()
        return path

# From the teminal prompts user to input a path
# Returns path the user inputs
# Returns "exit" if selection is cancled
def get_output_path():
    while True:
        path = input("Please enter the path to a directory to save geo-referenced files to: \nType 'Exit' to cancel\n").strip()

        if path.lower() == 'exit':
            print("Exiting the program.")
            return "exit"

        if not os.path.isdir(path):
            print("\nThe output path is not a valid directory. Please try again.")
        else:
            print(f"\nFolder selected: {path}")
            return path