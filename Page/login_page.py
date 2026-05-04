from selenium.webdriver.common.by import By
from Base.base_page import BasePage
import time


class LoginPage(BasePage):

    username_input = (By.ID, 'form_item_username')
    password_input = (By.ID, 'form_item_password')
    login_button = (By.CSS_SELECTOR, 'button.css-dev-only-do-not-override-1p3hq3p > span:nth-child(1)')
    login_result = (By.CSS_SELECTOR, '.ant-message-custom-content > span:nth-child(2)')
    other_show_hide_password = (By.CSS_SELECTOR, '.ant-input-suffix')

    def login(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)
        return self.text_of(self.login_result)
        
    def show_password(self, password):
        self.type(self.password_input, password)
        self.click(self.other_show_hide_password)   
        return self.get_attribute(self.password_input, 'type')

    def hide_password(self, password):
        self.type(self.password_input, password)
        self.click(self.other_show_hide_password) 
        self.click(self.other_show_hide_password)   
        return self.get_attribute(self.password_input, 'type')
         
