# This class includes all the function in La Liga App
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class LaLigaMobile:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.actions = TouchAction(self.driver)

    def click_allow(self):
        allow = self.driver.find_element(by=AppiumBy.ID, value="es.lfp.gi.main:id/btn_accept_cookies")
        allow.click()

    def get_login_button(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@resource-id='onboarding_welcome_button_login']/android.widget.Button")

    def click_login_button(self):
        self.get_login_button().click()

    def get_username_tab(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@text='LOGIN-0008']/android.view.View[1]/android.widget.EditText")

    def get_password_tab(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@text='LOGIN-0008']/android.view.View[2]/android.widget.EditText")

    def get_sign_in_button(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='SIGN IN']")

    def sign_in(self, username, password):
        self.get_username_tab().send_keys(username)
        self.get_password_tab().send_keys(password)
        self.get_sign_in_button().click()
        self.click_next()
        self.click_allow_permission()
        self.click_next()
        self.click_get_started()

    def click_next(self):
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='NEXT']").click()

    def click_allow_permission(self):
        self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button").click()

    def click_get_started(self):
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='GET STARTED']").click()

    def click_stats(self):
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Statistics']").click()

    def get_ranking(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='RANKING']")

    def click_ranking(self):
        self.get_ranking().click()

    def click_assists(self):
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Assists']").click()

    def get_player_name(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//androidx.compose.ui.platform.m1/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.TextView[4]")

    def get_player_assists(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//androidx.compose.ui.platform.m1/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.TextView[1]")

    def get_first_team(self):
        return self.driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='leaderboard_home_team']")[0]

    def click_more(self):
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='More']").click()

    def click_logout(self):
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='LOGOUT']").click()

    def click_accept_logout(self):
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@resource-id='dialog_button_continue']/android.widget.Button").click()

