from time import sleep
from unittest import TestCase
from appium import webdriver as app_webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver as sel_webdriver
from selenium.webdriver.chrome.service import Service
from pages.LaLigaHomePage import LaLigaHomePage
from pages.LaLigaMobile import LaLigaMobile
from pages.laLigaStatistics import LaLigaStatistics

appium_server_url_local = 'http://localhost:4723/wd/hub'

capabilities = dict(platformName="Android",
                    deviceName="Pixel7a",
                    udid="emulator-5554",
                    platformVersion="34",
                    appActivity="es.lfp.ui.view.main.MainActivity",
                    appPackage="es.lfp.gi.main")


class Test1(TestCase):
    def setUp(self):

        service_chrome = Service(r"C:\Users\Kramer\Documents\selenium1\chromedriver.exe")

        self.driver_sel = sel_webdriver.Chrome(service=service_chrome)

        self.driver_sel.get(r"https://www.laliga.com/en-IL")
        self.driver_sel.maximize_window()

        self.driver_sel.implicitly_wait(15)

        self.laLiga_home = LaLigaHomePage(self.driver_sel)

        self.laLiga_statistics = LaLigaStatistics(self.driver_sel)

        self.driver_app = app_webdriver.Remote(appium_server_url_local, capabilities)

        self.laliga_mobile = LaLigaMobile(self.driver_app)

        self.actions = TouchAction(self.driver_app)


    def tearDown(self):
        if self.driver_app:
            self.driver_app.quit()

    def test1(self):
        """Check if the data about the top 1 player in the assist table from La Liga Website is equal to the data about
        this player in La Liga Mobile Site. print the data from the website and check if the assists amount is equal"""
        # Web part
        self.laLiga_home.click_accept_cookies()
        # Enter to assists table
        self.laLiga_home.click_statistics()
        self.laLiga_statistics.click_assists()
        sleep(3)
        # Take the player assists details
        name = self.laLiga_statistics.get_best_assister_player_name().text
        print(name)
        assists_web = float(self.laLiga_statistics.get_best_assister_player_assists_num().text)
        print(f"Assists: {assists_web}")
        matches = float(self.laLiga_statistics.get_best_assister_player_games_num().text)
        print(f"Matches: {matches}")
        assist_per_game = float(self.laLiga_statistics.get_best_assister_player_assist_per_match().text)
        print(f"Assists Per Match: {assist_per_game}")
        # Check if the calculation of the assist per match is correct
        self.assertEqual(round(assists_web/matches, 2), assist_per_game)

        # Mobile part
        self.laliga_mobile.click_allow()
        # Log in process
        self.laliga_mobile.click_login_button()
        self.laliga_mobile.sign_in("itamars1000@gmail.com", "AaAa1234!")
        self.laliga_mobile.click_next()
        self.laliga_mobile.click_allow_permission()
        self.laliga_mobile.click_next()
        self.laliga_mobile.click_get_started()
        # Enter to the stats page
        self.laliga_mobile.click_stats()
        # move down to click for all stats tables
        self.actions.press(x=200, y=400).move_to(x=200, y=200).release().perform()
        self.laliga_mobile.click_ranking()
        # Move right to click om the assists table
        self.actions.press(x=750, y=360).move_to(x=150, y=360).release().perform()
        self.laliga_mobile.click_assists()
        # Take the data about the player
        print(self.laliga_mobile.get_player_name().text)
        assists_mobile = self.laliga_mobile.get_player_assists().text
        # Check if the assists amount equal
        self.assertEqual(int(assists_mobile), int(assists_web))
        sleep(3)
