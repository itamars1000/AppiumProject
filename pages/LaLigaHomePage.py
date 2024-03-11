# This class includes all the function in La Liga Home Page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class LaLigaHomePage:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_statistics_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='__next']/header/div[6]/div/div[3]")

    def click_statistics(self):
        self.get_statistics_button().click()

    def click_accept_cookies(self):
        self.driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").click()
