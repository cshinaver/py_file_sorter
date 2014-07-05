import tempfile
from os import rmdir
from shutil import rmtree
from filesort.file_sorter import FileSort


def before_all(context):
    file_sorter = FileSort()

    # Make sort dir
    file_sorter.sort_dir = tempfile.mkdtemp(
        prefix='tmp_sort_dir',
        dir='.',
        )
    print("Created test_dir at {0}".format(file_sorter.sort_dir))

    # Make movie_dir
    file_sorter.movie_dir = tempfile.mkdtemp(dir='.')
    print("Created movie_dir at {0}".format(file_sorter.movie_dir))

    context.file_sorter = file_sorter


def after_all(context):
    rmtree(context.file_sorter.sort_dir)
    rmtree(context.file_sorter.movie_dir)
