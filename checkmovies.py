from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def getMovieTitles():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

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

