# """Sorts downloads folder"""
import os
from shutil import move
DOWNLOAD_DIRECTORY_PATH = os.path.dirname(__file__)
SORTING_DIRECTORY_PATH = os.path.join(DOWNLOAD_DIRECTORY_PATH, 'files_to_sort')
my_file_path = os.path.join(SORTING_DIRECTORY_PATH, 'Episode 01 - The Empty Hearse.mkv')

def primary_sort(file_path):
    """First pass for sorting.
    Sorts file that might go to plex (video files) into a separate folder. Might just call secondary function for that file.
    """
    # Get file extension
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_path)
    file_extension = file_extension[1]

    # If file is a movie, move to sorted directory (Possibly Rename?)
    if file_extension in ('.mpeg', '.mpg', '.avi', '.mov', '.qt', '.wmv', '.mp4', '.ogm', '.mkv'):
        # TODO 1. Add check if sorted_files directory exists
        DESTINATION_PATH = os.path.join(DOWNLOAD_DIRECTORY_PATH, 'sorted_files')
        DESTINATION_PATH = os.path.join(DESTINATION_PATH, file_name)
        move(file_path, DESTINATION_PATH)
	print "%s was moved to %s" % (file_name, DESTINATION_PATH)


for sort_file in os.listdir(SORTING_DIRECTORY_PATH):
    sort_file_path = os.path.join(SORTING_DIRECTORY_PATH, sort_file)
    primary_sort(sort_file_path)
