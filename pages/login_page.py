from selenium.webdriver.common.by import By
from pages.base_page import *
from config import *


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")  
    PASSWORD_INPUT = (By.ID, "password")  
    LOGIN_BUTTON = (By.ID, "login-button")  
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")  

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(BASE_URL)

    def login(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text
