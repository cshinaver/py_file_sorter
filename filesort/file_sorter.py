#!/usr/bin/python
"""Sorts downloads folder"""
import os
from shutil import move, rmtree


class FileSort:
    sort_dir = ''
    movie_dir = ''
    tv_show_dir = ''
    lynda_dir = ''
    music_dir = ''
    app_dir = ''

    #TODO Write function that takes args like sort_downloads,
    # sort_TV_Shows, sort_Movies
    def primary_sort(self, file_path):
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
                #remove_dirtree(file_path)
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
                file_path = os.path.join(self.sort_dir, file)
                self.primary_sort(file_path)
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
    # if __name__ == "__main__":
    #     main()
