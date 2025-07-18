import pytest  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  


@pytest.fixture(scope="function")  
def browser():  
    driver = webdriver.Firefox()
    yield driver
    driver.quit()  