
from Pages.BasePage import BasePage
from Utilities import configReader


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fillForm(self,email,cemail,Fname,Lname, country, password,cpassword):
        self.click("login_XPATH")
        self.click("create_account_XPATH")
        self.click("email_XPATH")
        self.type("email_XPATH", email)
        self.click("cemail_XPATH")
        self.type_wait("cemail_XPATH", cemail)
        self.type("Fname_XPATH",Fname)
        self.type("Lname_XPATH", Lname)
        self.type("password_XPATH",password)
        self.type("cpassword_XPATH",cpassword)
        self.select("country_XPATH", country)
      #  self.click("submit_XPATH")
