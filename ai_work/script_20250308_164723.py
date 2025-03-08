```python
import os
import shutil

def organize_files(source_dir, destination_dir):
    """
    Organize files from source directory to destination directory based on their file extension.

    Parameters:
    source_dir (str): Path to the source directory.
    destination_dir (str): Path to the destination directory.

    Returns:
    None
    """
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)

    # Iterate through files in source directory
    for file_name in os.listdir(source_dir):
        source_path = os.path.join(source_dir, file_name)

        if os.path.isfile(source_path):
            # Get file extension
            _, extension = os.path.splitext(file_name)

            # Make directory for the file extension if it doesn't exist
            extension_dir = os.path.join(destination_dir, extension.lstrip('.'))
            if not os.path.exists(extension_dir):
                os.mkdir(extension_dir)

            destination_path = os.path.join(extension_dir, file_name)

            # Move file to the corresponding directory
            shutil.move(source_path, destination_path)

    print("Files organized successfully!")

# Example usage
source_directory = "source_folder"
destination_directory = "organized_files"
organize_files(source_directory, destination_directory)
```