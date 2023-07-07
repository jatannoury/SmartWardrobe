from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

from config.endpoints import Endpoints

def scrape_shutterstock():
    driver = webdriver.Chrome()

    driver.get(Endpoints.shutterstock_endpoint+"/classic-full-outfit")
    time.sleep(2)  # Wait for the page to load

    # Scroll to the bottom of the page
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for the page to load after scrolling
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    results = soup.select('[href*=image-photo]')
    links = [element['href'] for element in results if element.has_attr('href')]
    images_links = [link for link in links if link.startswith("https") == False]
    print(images_links)
    print(len(images_links))

    # Close the Selenium driver
    driver.quit()

scrape_shutterstock()
