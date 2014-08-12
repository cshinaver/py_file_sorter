#!/usr/bin/python
"""Sorts downloads folder"""
import os
from shutil import move, rmtree
import argparse


MOVIE_FILE_EXTENTIONS = (
    '.mpeg',
    '.mpg',
    '.avi',
    '.mov',
    '.qt',
    '.wmv',
    '.mp4',
    '.ogm',
    '.mkv',
    )


class FileSort:
    sort_dir = ''
    movie_dir = ''
    tv_show_dir = ''
    lynda_dir = ''
    music_dir = ''
    app_dir = ''

    def __init__(self, args):
        # Make list of dir arguments
        directory_arguments = [
            attr for attr in dir(args)
            if 'dir' in attr and
            isinstance(
                getattr(
                    self,
                    attr
                    ),
                str)]

        # Set dir properties for given dir arguments
        for directory in directory_arguments:
            directory_location = getattr(args, directory)
            setattr(self, directory, directory_location)


    #TODO Write function that takes args like sort_downloads,
    # sort_TV_Shows, sort_Movies
    def primary_sort(self, file_path):
        #TODO Add sorting for Other things that aren't videos
        """
        Sorts given filepath into Movies and Learning Videos
        """

        # Sort path
        working_full_path = os.path.join(file_path, os.pardir)
        working_sort_path = os.path.abspath(working_full_path)

        # Get file extension
        file_name = os.path.basename(file_path)
        file_extension = os.path.splitext(file_path)
        file_extension = file_extension[1]

        # Movie Selection and Sorting
        if file_extension in MOVIE_FILE_EXTENTIONS:
            # TODO 1. Possibly add something to differentiate between
            # TV Shows and
            # Movies (if not Lynda.com files)
            if "Lynda" in file_name and self.lynda_dir:
                self.directory_exists(self.lynda_dir)
                move(file_path, self.lynda_dir)
                print('{0} was moved to {1}'.format(
                    file_name,
                    self.lynda_dir,
                    ))
            elif "Lynda" in file_name and not self.lynda_dir:
                return
            else:
                # TODO 2. Also, remove directory after transfer

                self.directory_exists(self.movie_dir)
                move(file_path, self.movie_dir)
                print('{0} was moved to {1}'.format(
                    file_name,
                    self.movie_dir,
                    ))

    def directory_exists(self, directory_path):
        """Checks if directory exists. Creates it if test fails"""
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)
            print('{0} did not exist, so it was created'.format(
                directory_path,
                ))

    def main_sorter(self):
        """Main function"""
        print("Beginning file sort...")
        # Recursively sort SORTING_DIRECTORY_PATH
        for sort_dir, dirs, files in os.walk(self.sort_dir):
            print("Checking " + str(sort_dir))
            for file in files:
                file_path = os.path.join(sort_dir, file)
                self.primary_sort(file_path)
        self.remove_sorted_dirtree(self.sort_dir)
        print("Sorting Complete.")

    def remove_sorted_dirtree(self, sort_path):
        #TODO Finish this function
        """Removes parent dirtree for given file_path"""
        if ".sorted" in os.listdir(sort_path):
            print "yay"
    # my_file_path = os.path.join(SORTING_DIRECTORY_PATH, 'mah_dir')
    # my_file_path = os.path.join(my_file_path, 'show.mkv')
    # remove_dirtree(my_file_path)


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--sort-dir',
        dest='sort_dir',
        help='String to sort dir',
        )
    parser.add_argument(
        '--movie-dir',
        dest='movie_dir',
        help='String to movie dir',
        )

    return parser.parse_args(args)


def main():
    args = parse_args()
    file_sorter = FileSort(args)
    file_sorter.main_sorter()


if __name__ == "__main__":
    main()
