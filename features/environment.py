import tempfile
from os import rmdir


def before_all(context):
    # Make sort dir
    context.tmp_sort_dir_path = tempfile.mkdtemp(
        prefix='tmp_sort_dir',
        dir='.',
        )
    print("Created test_dir at {0}".format(context.tmp_sort_dir_path))

    # Make movie_dir
    context.tmp_movie_dir_path = tempfile.mkdtemp(dir='.')
    print("Created movie_dir at {0}".format(context.tmp_movie_dir_path))


def after_all(context):
    rmdir(context.tmp_sort_dir_path)
    rmdir(context.tmp_movie_dir_path)
