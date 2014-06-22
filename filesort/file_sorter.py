#!/usr/bin/python
"""Sorts downloads folder"""
import os
from shutil import move, rmtree
DOWNLOAD_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
# Currently, file executes as if SORTING_DIRECTORY exists
# in DOWNLOAD_DIRECTORY. Set sorting directory to dowload directory to
# sort download directory path

SORTING_DIRECTORY_PATH = os.path.join(DOWNLOAD_DIRECTORY_PATH, 'files_to_sort')
MOVIE_DESTINATION_PATH = os.path.join(DOWNLOAD_DIRECTORY_PATH, 'Movies')
TV_SHOW_DESTINATION_PATH = os.path.join(DOWNLOAD_DIRECTORY_PATH, 'TV Shows')
LEARNING_VIDEOS_DESTINATION_PATH = os.path.join(
    DOWNLOAD_DIRECTORY_PATH,
    'Learning Videos',
    )


class FileSort:
    name = "test"

#TODO Write function that takes args like sort_downloads,
# sort_TV_Shows, sort_Movies


def primary_sort(file_path):
    #TODO Add sorting for Other things that aren't videos
    """
    Sorts given filepath into Movies and Learning Videos
    """
    # Get file extension
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_path)
    file_extension = file_extension[1]

    # Movie Selection and Sorting
    if file_extension in ('.mpeg',
                          '.mpg',
                          '.avi',
                          '.mov',
                          '.qt',
                          '.wmv',
                          '.mp4',
                          '.ogm',
                          '.mkv'
                          ):
        # TODO 1. Possibly add something to differentiate between TV Shows and
        # Movies (if not Lynda.com files)
        if file_name.find("Lynda.com") != -1:
            directory_exists(LEARNING_VIDEOS_DESTINATION_PATH)
            move(file_path, LEARNING_VIDEOS_DESTINATION_PATH)
            print('{0} was moved to {1}'.format(
                file_name,
                LEARNING_VIDEOS_DESTINATION_PATH,
                ))
        else:
            # TODO 2. Also, remove directory after transfer

            directory_exists(MOVIE_DESTINATION_PATH)
            move(file_path, MOVIE_DESTINATION_PATH)
            remove_dirtree(file_path)
            print('{0} was moved to {1}'.format(
                file_name,
                MOVIE_DESTINATION_PATH,
                ))


def directory_exists(directory_path):
    """Checks if directory exists. Creates it if test fails"""
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path)
        print('{0} did not exist, so it was created'.format(directory_path))


def main():
    """Main function"""
    print("Beginning file sort...")
    # Recursively sort SORTING_DIRECTORY_PATH
    for sort_dir, dirs, files in os.walk(SORTING_DIRECTORY_PATH):
        print("Checking " + str(sort_dir))
        for file in files:
            file_path = os.path.join(DOWNLOAD_DIRECTORY_PATH, sort_dir)
            file_path = os.path.join(file_path, file)
            primary_sort(file_path)
    print("Sorting Complete.")


def remove_dirtree(file_path):
    #TODO Finish this function
    """Removes parent dirtree for given file_path"""
    len_sort_dir = len(SORTING_DIRECTORY_PATH)
    print(file_path)
    print(file_path[len_sort_dir:])

# my_file_path = os.path.join(SORTING_DIRECTORY_PATH, 'mah_dir')
# my_file_path = os.path.join(my_file_path, 'show.mkv')
# remove_dirtree(my_file_path)
if __name__ == "__main__":
    main()
