from Pages.BasePage import BasePage
from Utilities import configReader


class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def fill_login(self,email,password):
        self.click("login_XPATH")
        self.type("Email_login_XPATH", email)
        self.type("Email_pass_XPATH",password)
        self.click("Login_button_XPATH")

      #  self.click("submit_XPATH")
