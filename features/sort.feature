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
    
    Scenario: Lynda movie
        Given a sort path
        And a Lynda path
        When the file is a Lynda movie
        Then the file should be moved to the Lynda Folder

    # Scenario: TV Show
    #     Given a sort path
    #     And a TV Show path
    #     When the file is a movie file
    #     And it is smaller than 400MB
    #     Then the file should be moved to the TV Shows Folder

