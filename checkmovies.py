from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from subprocess import CREATE_NO_WINDOW

def getMovieTitles():
    service = Service('./chromedriver')
    service.creationflags = CREATE_NO_WINDOW

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options, service=service)
    driver.get("https://www.statecinemas.co.nz")

    moviesSection = driver.find_element(By.ID, "printArea")
    moviePosters = moviesSection.find_elements(By.CLASS_NAME, "posters")

    titles = set()
    for moviePoster in moviePosters:    
        movieLink = moviePoster.find_element(By.CLASS_NAME, "movie-link")
        movieTitle = movieLink.find_element(By.TAG_NAME, "h2")

        titles.add(movieTitle.get_attribute('innerHTML'))

    driver.close()
    driver.quit()

    return titles

