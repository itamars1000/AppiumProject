# This class includes all the function in La Liga Standings Page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class LaLigaStandingsPage:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_first_place_team(self):
        return self.driver.find_element(By.XPATH, "//*[@id='__next']/div[6]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/p")
