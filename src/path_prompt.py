import os
import time
import sys  # To flush the output immediately

while True:
    # Step 1: Get the first directory from the user
    path = input("Please enter the path to a directory: \nType 'Exit' to cancel\n").strip()

    if path.lower() == 'exit':
        print("Exiting the program.")
        break

    if not os.path.isdir(path):
        print("The path is not a valid directory. Please try again.")
        continue

    if not os.listdir(path):
        print("The folder is empty. Please select a non-empty folder.")
    else:
        files = os.listdir(path)
        print(f"Folder selected: {path}")

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
            total_size_gb = total_tif_size / (1024 * 1024 * 1024)
            if total_size_gb >= 1:
                print(f"Total size of TIF files: {total_size_gb:.2f} GB")
            else:
                total_size_mb = total_tif_size / (1024 * 1024)
                print(f"Total size of TIF files: {total_size_mb:.2f} MB")
        else:
            print("No TIF files found.")

        print(f"Number of non-TIF files found: {len(other_files)}")

        # Step 2: Get the second directory for output
        output_dir = input("Please enter the path to a directory where you want to create text files: \nType 'Exit' to cancel\n").strip()

        if output_dir.lower() == 'exit':
            print("Exiting the program.")
            break

        if not os.path.isdir(output_dir):
            print("The output path is not a valid directory. Please try again.")
            continue

        # Step 3: Loop through each TIFF file and create a "hello world" text file in the output directory
        for idx, tif_file in enumerate(tif_files, 1):
            # Print progress in the same line using carriage return
            print(f"\rProcessing file {idx} of {len(tif_files)}", end="")

            # Flush the output buffer to force print the line in real-time
            sys.stdout.flush()

            # Pause for 2 seconds
            time.sleep(2)

            # Construct the full path for the new text file
            text_filename = f"{os.path.splitext(tif_file)[0]}.txt"
            text_file_path = os.path.join(output_dir, text_filename)

            # Create the text file and write "hello world" in it
            with open(text_file_path, 'w') as f:
                f.write("hello world")

        # Ensure the progress is completed by moving to the next line after final processing
        print("\nAll text files created successfully.")
        break
