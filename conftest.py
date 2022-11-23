import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def init_driver():
    web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield web_driver
    web_driver.quit()