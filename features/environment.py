import tempfile
from shutil import rmtree
from filesort.file_sorter import FileSort


def before_all(context):
    args = []
    file_sorter = FileSort(args)
    # Make tmp_files dir
    context.tmp_files_dir = tempfile.mkdtemp(
        prefix='tmp_files',
        )
    print("Created tmp_files dir at {0}".format(context.tmp_files_dir))

    context.file_sorter = file_sorter


def after_all(context):
    rmtree(context.tmp_files_dir)
