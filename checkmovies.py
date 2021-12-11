import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from subprocess import CREATE_NO_WINDOW

def getMovieTitles():
    """Method to scrape the State Cinema website for all the currently showing titles"""
    # Create a new service with no window 
    service = Service('./chromedriver')
    service.creationflags = CREATE_NO_WINDOW

    # Create the browser in headless mode so it can run in the background
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options, service=service)

    # Load the state cinema websit
    driver.get("https://www.statecinemas.co.nz")

    # Find the area where movie data is stored
    moviesSection = driver.find_element(By.ID, "printArea")
    moviePosters = moviesSection.find_elements(By.CLASS_NAME, "posters")

    titles = set()
    for moviePoster in moviePosters:    
        # Find the link to the movie and from that the title
        movieLink = moviePoster.find_element(By.CLASS_NAME, "movie-link")
        movieTitle = movieLink.find_element(By.TAG_NAME, "h2")

        titles.add(movieTitle.get_attribute('innerHTML'))

    driver.close()
    driver.quit()

    return titles

def inOpenHours(now):
    start = datetime.time(10, 30, 0)
    end = datetime.time(23, 30, 0)

    if start <= end:
        return start <= now < end
    else:
        return start <= now or now < end