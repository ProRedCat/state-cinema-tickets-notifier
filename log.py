import os.path

from checkmovies import *

def logTitle(title):
    """Method to log the title into a file called movies.txt"""
    file = open("movies.txt", "a")
    file.write(title + "\n")
    file.close()

def loadTitles():
    """Method to load the titles on program start"""
    titles = set()

    # If the movies.txt file does exist (program has already been run before)
    if(os.path.exists("movies.txt")):
        # Create movies.txt and start writing to it 
        file = open("movies.txt", "r")

        # Get each title and remove the \n on the end and add to titles set
        for title in file:
            titles.add(title.removesuffix("\n"))

        file.close()
    else: # Else this is the first time start up 
        # Get all current movies showing
        titles = getMovieTitles()

        # Log these titles
        for title in titles:
            logTitle(title)

    return titles

