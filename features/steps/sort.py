"""
Feature: Download_Sorter (Natural Language)
    In order to have a clean and sorted downloads folder,
    As the admin
    I want the downloads to be moved based on type to
        the set destinations. In my case, the media server


    Scenario: Movie
        Given a sort path
        And a movie path
        When the file is a movie
        Then the file should be moved to the Movie Folder
"""
from behave import *  # noqa
import tempfile
from os.path import isdir, exists
from os import path
from filesort.file_sorter import FileSort, parse_args


@given(u'a subdirectory')
def step_given_a_subdirectory(context):
    # Make sub_dir
    context.sub_dir = tempfile.mkdtemp(
        prefix='tmp_sub_dir',
        dir=context.file_sorter.sort_dir,
        )
    print("Created sub_dir at {0}".format(context.sub_dir))
    assert isdir(context.sub_dir)


@given(u'a subdirectory in the subdirectory')
def step_given_a_subdirectory_in_the_subdirectory(context):
    # Make second sub_dir
    context.second_sub_dir = tempfile.mkdtemp(
        prefix='tmp_second_sub_dir',
        dir=context.sub_dir,
        )
    print("Created second_sub_dir at {0}".format(context.second_sub_dir))
    assert isdir(context.second_sub_dir)


@given(u'a movie file in the subdirectory')
def step_movie_file_in_sub_dir(context):
    # Create movie file in subdirectory
    context.tmp_movie_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        suffix='.mov',
        delete=False,
        dir=context.sub_dir,
        )
    assert exists(context.tmp_movie_file.name)


@given(u'two movie files in the subdirectory')
def step_given_two_movie_files_in_the_subdirectory(context):
    context.first_tmp_movie_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        suffix='.mov',
        delete=False,
        dir=context.sub_dir,
        )
    assert exists(context.first_tmp_movie_file.name)

    context.second_tmp_movie_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        suffix='.mov',
        delete=False,
        dir=context.sub_dir,
        )
    assert exists(context.second_tmp_movie_file.name)


@given(u'two movie files')
def step_given_two_movie_files(context):
    context.first_tmp_movie_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        suffix='.mov',
        delete=False,
        dir=context.file_sorter.sort_dir,
        )
    assert exists(context.first_tmp_movie_file.name)

    context.second_tmp_movie_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        suffix='.mov',
        delete=False,
        dir=context.file_sorter.sort_dir,
        )
    assert exists(context.second_tmp_movie_file.name)


@given(u'a text file in the subdirectory')
def step_given_a_text_file_in_the_subdirectory(context):
    # Create text file in subdirectory
    context.tmp_txt_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        suffix='.txt',
        delete=False,
        dir=context.sub_dir,
        )
    assert exists(context.tmp_txt_file.name)


@given(u'an image file in the second subdirectory')
def step_impl(context):
    # Create jpeg file in subdirectory
    context.tmp_txt_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        suffix='.jpeg',
        delete=False,
        dir=context.second_sub_dir,
        )
    assert exists(context.tmp_txt_file.name)


@given(u'a sort path argument')
def step_sort_path_argument_given(context):
    sort_dir = context.file_sorter.sort_dir
    args = ['--sort-dir', sort_dir]

    if not hasattr(context, 'args'):
        context.args = args
    elif hasattr(context, 'args'):
        context.args.extend(args)
    assert sort_dir in context.args


@given(u'a movie path argument')
def step_movie_path_argument_given(context):
    movie_dir = context.file_sorter.movie_dir
    args = ['--movie-dir', movie_dir]

    if not hasattr(context, 'args'):
        context.args = args
    elif hasattr(context, 'args'):
        context.args.extend(args)
    assert movie_dir in context.args


@given('a sort path')
def step_a_sort_path(context):
    # Make sort dir
    context.file_sorter.sort_dir = tempfile.mkdtemp(
        prefix='tmp_sort_dir',
        dir=context.tmp_files_dir,
        )
    print("Created test_dir at {0}".format(context.file_sorter.sort_dir))
    assert isdir(context.file_sorter.sort_dir)


@given('a movie path')
def step_a_movie_path(context):
    # Make movie_dir
    context.file_sorter.movie_dir = tempfile.mkdtemp(
        prefix='tmp_movie_dir',
        dir=context.tmp_files_dir,
        )
    print("Created movie_dir at {0}".format(context.file_sorter.movie_dir))
    assert isdir(context.file_sorter.movie_dir)


@given('a Lynda path')
def step_a_lynda_path(context):
    # Make lynda movie_dir
    context.file_sorter.lynda_dir = tempfile.mkdtemp(
        prefix='tmp_lynda_dir',
        dir=context.tmp_files_dir,
        )
    print("Created lynda_movie_dir at {0}".format(
        context.file_sorter.lynda_dir
        ))
    assert isdir(context.file_sorter.lynda_dir)


@given(u'a movie file')
def step_file_is_movie(context):
    context.tmp_movie_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        suffix='.mov',
        delete=False,
        dir=context.file_sorter.sort_dir,
        )
    assert exists(context.tmp_movie_file.name)


@given(u'a Lynda movie file')
def step_a_lynda_movie(context):
    context.tmp_lynda_movie_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        prefix='Lynda.com',
        suffix='.mov',
        delete=False,
        dir=context.file_sorter.sort_dir,
        )
    assert exists(context.tmp_lynda_movie_file.name)


@given(u'a music file')
def step_music_file_given(context):
    context.tmp_music_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        prefix='',
        suffix='.mp3',
        delete=False,
        dir=context.file_sorter.sort_dir,
        )
    assert exists(context.tmp_music_file.name)


@when(u'only a movie path is given')
def step_only_movie_path_given(context):
    context.file_sorter.lynda_dir = ''
    fs = context.file_sorter

    assert not any([
        fs.lynda_dir,
        fs.music_dir,
        fs.app_dir,
        fs.tv_show_dir,
    ])


@when(u'the sorter is started')
def step_sorter_start(context):
    context.file_sorter.main_sorter()


@when(u'the sorter is started with arguments')
def step_sorter_started_with_arguments(context):
    args = parse_args(context.args)
    file_sorter = FileSort(args)
    file_sorter.main_sorter()


@then(u'the Lynda movie should not be moved')
def step_Lynda_movie_file_not_moved(context):
    assert exists(context.tmp_lynda_movie_file.name)


@then(u'the music file should not be moved')
def step_music_file_not_moved(context):
    assert exists(context.tmp_music_file.name)


@then('the movie file should be moved to the Movie Folder')
def step_movie_file_moved(context):
    # Test
    file_name = path.basename(context.tmp_movie_file.name)
    new_file_name = path.join(context.file_sorter.movie_dir, file_name)
    assert exists(new_file_name)


@then('the Lynda movie file should be moved to the Lynda Folder')
def step_lynda_file_moved(context):
    # Test
    file_name = path.basename(context.tmp_lynda_movie_file.name)
    new_file_name = path.join(context.file_sorter.lynda_dir, file_name)
    assert exists(new_file_name)


@then(u'two movie files should be moved to the Movie Folder')
def step_two_movie_files_moved(context):
    # First movie file
    file_name = path.basename(context.first_tmp_movie_file.name)
    new_file_name = path.join(context.file_sorter.movie_dir, file_name)
    assert exists(new_file_name)

    # Second movie file
    file_name = path.basename(context.second_tmp_movie_file.name)
    new_file_name = path.join(context.file_sorter.movie_dir, file_name)
    assert exists(new_file_name)


@then(u'the subdirectory should be deleted')
def step_is_subdirectory_deleted(context):
    assert False
