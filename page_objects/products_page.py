from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class Products(BasePage):

    def get_title(self):
        return self.driver.find_element(By.CLASS_NAME, "title").text




