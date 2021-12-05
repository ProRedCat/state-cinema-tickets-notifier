import os.path

from checkmovies import *

def logTitle(title):
    file = open("movies.txt", "a")
    file.write(title + "\n")
    file.close()

def loadTitles():
    titles = set()

    if(os.path.exists("movies.txt")):
        file = open("movies.txt", "r")

        for title in file:
            titles.add(title.removesuffix("\n"))

        file.close()
    else:
        titles = getMovieTitles()

        for title in titles:
            logTitle(title)

    return titles

