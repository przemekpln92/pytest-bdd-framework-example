from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class Login(BasePage):

    def go_to_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def fill_form_and_log_in(self, username, password):
        username = self.driver.find_element(By.ID, "user-name").send_keys(username)
        password = self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
