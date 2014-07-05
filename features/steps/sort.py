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


@when('the file is a movie')
def step_file_is_movie(context):
    context.tmp_movie_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        suffix='.mov',
        delete=False,
        dir=context.file_sorter.sort_dir,
        )
    assert exists(context.tmp_movie_file.name)


@then('the file should be moved to the Movie Folder')
def step_file_moved(context):
    context.file_sorter.main_sorter()

    # Test
    file_name = path.basename(context.tmp_movie_file.name)
    new_file_name = path.join(context.file_sorter.movie_dir, file_name)
    assert exists(new_file_name)


@given('a Lynda path')
def step_a_lynda_path(context):
    assert isdir(context.file_sorter.lynda_dir)


@when('the file is a Lynda movie')
def step_a_lynda_movie(context):
    context.tmp_movie_file = tempfile.NamedTemporaryFile(
        mode='w+b',
        prefix='Lynda.com',
        suffix='.mov',
        delete=False,
        dir=context.file_sorter.sort_dir,
        )
    assert exists(context.tmp_movie_file.name)


@then('the file should be moved to the Lynda Folder')
def step_impl(context):
    context.file_sorter.main_sorter()

    # Test
    file_name = path.basename(context.tmp_movie_file.name)
    new_file_name = path.join(context.file_sorter.lynda_dir, file_name)
    assert exists(new_file_name)

# @given('a TV Show path')
# def step_impl(context):
#     assert False


# @when('the file is a movie file')
# def step_impl(context):
#     assert False


# @when('it is smaller than 400MB')
# def step_impl(context):
#     assert False


# @then('the file should be moved to the TV Shows Folder')
# def step_impl(context):
#     assert False
