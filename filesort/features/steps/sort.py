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
from behave import *
from 

@given('a sort path')
def step_impl(context):
    assert 2 ==3

@given('a movie path')
def step_impl(context):
    assert False

@when('the file is a movie')
def step_impl(context):
    assert False

@then('the file should be moved to the Movie Folder')
def step_impl(context):
    assert False

