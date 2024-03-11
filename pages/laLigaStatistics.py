# This class includes all the function in La Liga Statistics Page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LaLigaStatistics:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_assists_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='__next']/div[6]/div[2]/div[1]/div[1]/a[4]")

    def click_assists(self):
        self.get_assists_button().click()

    def get_best_assister_player_name(self):
        return self.driver.find_element(By.XPATH, "//*[@id='__next']/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[3]")

    def get_best_assister_player_assists_num(self):
        return self.driver.find_element(By.XPATH, "//*[@id='__next']/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]")

    def get_best_assister_player_games_num(self):
        return self.driver.find_element(By.XPATH, "//*[@id='__next']/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[6]")

    def get_best_assister_player_assist_per_match(self):
        return self.driver.find_element(By.XPATH, "//*[@id='__next']/div[6]/div[2]/div[2]/div/table/tbody/tr[1]/td[7]")
