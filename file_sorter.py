# """Sorts downloads folder"""
import os
from shutil import move, rmtree
DOWNLOAD_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
SORTING_DIRECTORY_PATH = os.path.join(DOWNLOAD_DIRECTORY_PATH, 'files_to_sort')
MOVIE_DESTINATION_PATH = os.path.join(DOWNLOAD_DIRECTORY_PATH, 'Movies')
TV_SHOW_DESTINATION_PATH = os.path.join(DOWNLOAD_DIRECTORY_PATH, 'TV Shows')
LEARNING_VIDEOS_DESTINATION_PATH = os.path.join(DOWNLOAD_DIRECTORY_PATH, 'Learning Videos')


def primary_sort(file_path):
    """
    Determing file type and sorting
    """
    # Get file extension
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_path)
    file_extension = file_extension[1]

    # Movie Selection and Sorting
    if file_extension in ('.mpeg', '.mpg', '.avi', '.mov', '.qt', '.wmv', '.mp4', '.ogm', '.mkv'):
        # TODO 1. Possibly add something to differentiate between TV Shows and
        # Movies (if not Lynda.com files)
        if (file_name.find("Lynda.com") != -1):
            directory_exists(LEARNING_VIDEOS_DESTINATION_PATH)
            move(file_path, LEARNING_VIDEOS_DESTINATION_PATH)
            print "%s was moved to %s" % (file_name, LEARNING_VIDEOS_DESTINATION_PATH)
        else:
            # TODO 2. Also, remove directory after transfer

            directory_exists(MOVIE_DESTINATION_PATH)
            move(file_path, MOVIE_DESTINATION_PATH)
            print "%s was moved to %s" % (file_name, MOVIE_DESTINATION_PATH)


def directory_exists(directory_path):
    """Checks if directory exists. Creates it if test fails"""
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path)
        print "%s did not exist, so it was created" % (directory_path)


def main():
    """Main function"""
    # Recursively sort SORTING_DIRECTORY_PATH
    for sort_dir, dirs, files in os.walk(SORTING_DIRECTORY_PATH):
        for file in files:
            file_path = os.path.join(DOWNLOAD_DIRECTORY_PATH, sort_dir)
            file_path = os.path.join(file_path, file)
            primary_sort(file_path)
main()
