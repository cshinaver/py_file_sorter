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
from filesort.file_sorter import FileSort


@given('a sort path')
def step_a_sort_path(context):
    assert 2 == 3


@given('a movie path')
def step_a_movie_path(context):
    assert False


@when('the file is a movie')
def step_file_is_movie(context):
    assert False


@then('the file should be moved to the Movie Folder')
def step_file_moved(context):
    assert False
