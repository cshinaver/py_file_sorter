import tempfile
from os import rmdir


def before_all(context):
    context.tmp_sort_dir_path = tempfile.mkdtemp(
        prefix='tmp_sort_dir',
        dir='.',
        )
    print("Created test_dir at {0}".format(context.tmp_sort_dir_path))


def after_all(context):
    rmdir(context.tmp_sort_dir_path)
