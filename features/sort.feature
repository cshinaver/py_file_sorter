Feature: Download_Sorter (Natural Language)
    In order to have a clean and sorted downloads folder,
    As the admin
    I want the downloads to be moved based on type to 
        the set destinations. In my case, the media server


    Scenario: Movie
        Given a sort path 
        And a movie path
        And a movie file
        When the sorter is started
        Then the movie file should be moved to the Movie Folder
    
    Scenario: Lynda movie
        Given a sort path
        And a Lynda path
        And a Lynda movie file
        When the sorter is started
        Then the Lynda movie file should be moved to the Lynda Folder

    Scenario: Sort and only Movie directory given
        Given a sort path
        And a movie path
        And a movie file
        And a music file
        And a Lynda movie file
        When only a movie path is given
        And the sorter is started
        Then the movie file should be moved to the Movie Folder
        And the Lynda movie should not be moved 
        And the music file should not be moved

    Scenario: Test input
        Given a sort path
        And a sort path argument
        And a movie path
        And a movie path argument
        And a movie file
        When the sorter is started with arguments
        Then the movie file should be moved to the Movie Folder

    Scenario: Multiple Movies
        Given a sort path
        And a movie path
        And two movie files
        When the sorter is started
        Then two movie files should be moved to the Movie Folder

    Scenario: Subdirectories
        Given a sort path
        And a subdirectory
        And a movie file in the subdirectory
        And a movie path
        When the sorter is started
        Then the movie file should be moved to the Movie Folder

    Scenario: Movie Folder
        Given a sort path
        And a movie path
        And a subdirectory
        And two movie files in the subdirectory
        And a text file in the subdirectory
        And a subdirectory in the subdirectory
        And an image file in the second subdirectory
        When the sorter is started
        Then two movie files should be moved to the Movie Folder
        And the subdirectory should be deleted

    # Scenario: TV Show
    #     Given a sort path
    #     And a TV Show path
    #     When the file is a movie file
    #     And it is smaller than 400MB
    #     Then the file should be moved to the TV Shows Folder
