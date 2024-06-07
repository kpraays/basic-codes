"""
Reorganize pictures for oneDrive windows. 
It will put the pictures in folder based on months and year depending on the timestamp in their names.
Standard naming expected: example - IMG-20230522-WAXXXX.jpg
Extensions expected: .jpg, .png, .mp4
Usage: python reorganize.py \location\camera\folder\to\be\reorganized
"""

import os
import argparse

def get_files(photos_path):
    """
    Scans a directory recursively to find and list all photo and video files.

    Args:
        photos_path (str): The path to the directory where photo and video files are searched.

    Returns:
        list of str: Sorted list of the full paths to all files with .jpg, .png, or .mp4 extensions found within the given directory.
    """
    assert os.path.isdir(photos_path)
    list_of_photos = []

    for path, directories, filenames in os.walk(photos_path):
        for filename in filenames:
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".mp4"):
                list_of_photos.append(os.path.join(path, filename))
                           
    print(f"Total number of items retrieved: {len(list_of_photos)}")
    return sorted(list_of_photos)

def process_files(list_of_photos, photos_path):
    """
    Creates the destination paths if they do not exist and adds them to a dict.

    Args:
        list of str: Sorted list of the full paths to all files with .jpg, .png, or .mp4 extensions.

    Returns:
        Dict of dest folders as keys and files to be moved as values.
    """
    sorted_files = {}
    for filepath in list_of_photos:
        file = filepath.split(os.path.sep)[-1]
        if "_" in file:
            date = file.split("_")[1]
        else:
            date = file.split("-")[1]
        year = date[0:4]
        month = date[4:6]
             
        # create month directory if it does not exist
        
        parent = os.path.join(photos_path, year)
        if not os.path.isdir(parent):
            os.mkdir(parent)
        
        child = os.path.join(photos_path, year, month)
        if not os.path.isdir(child):
            os.mkdir(child)
        
        if not sorted_files.get(child):
            sorted_files[child] = [filepath]
        else:
            sorted_files[child].append(filepath)

    print(f"The month wise organised folders are: {sorted_files.keys()}")
    return sorted_files


def move_files(sorted_files):
    """
    Moves files from source to destination.

    Args:
        Dict of dest folders as keys and files to be moved as values.
        
    Returns:
        None
    """
    for key, value in sorted_files.items():
        for filename in value:
            destination = os.path.join(key, filename.split(os.path.sep)[-1])
            os.rename(filename, destination)
            print(f"Moving file {filename} to {destination}.")

def main():
    parser = argparse.ArgumentParser(
        prog="reorganize",
        description="""
        Reorganize pictures for oneDrive windows. 
        It will put the pictures in folder based on months and year depending on the timestamp in their names.
        Standard naming expected: example - IMG-20230522-WAXXXX.jpg
        Extensions expected: .jpg, .png, .mp4
        Usage: python reorganize.py \location\camera\folder\to\be\reorganized
        """,
        epilog="Example: reorganize \\path\\to\\your\\pics"
    )
    
    parser.add_argument("photos_path", help="Path to the pictures to be reorganized.")
    
    args = parser.parse_args()
    print(f"Location of the photos: {args.photos_path}")
    
    list_of_photos = get_files(args.photos_path)
    path_dict = process_files(list_of_photos, args.photos_path)
    move_files(path_dict)


if __name__ == "__main__":
    main()