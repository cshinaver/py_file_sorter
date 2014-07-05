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


@given('a sort path')
def step_a_sort_path(context):
    assert isdir(context.file_sorter.sort_dir)


@given('a movie path')
def step_a_movie_path(context):
    assert isdir(context.file_sorter.movie_dir)


@given('a Lynda path')
def step_a_lynda_path(context):
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
    fs = context.file_sorter
    assert any([
        fs.lynda_dir,
        fs.music_dir,
        fs.app_dir,
        fs.tv_show_dir,
    ])


@when(u'the sorter is started')
def step_sorter_start(context):
    context.file_sorter.main_sorter()


@then(u'the Lynda movie should not be moved')
def step_Lynda_movie_file_not_moved(context):
    assert exists(context.tmp_lynda_movie_file.name)


@then(u'the music file should not be moved')
def step_music_file_not_moved(context):
    assert False


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
