import allure
import pytest
from Pages.RegistrationPage import RegistrationPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider

import logging
from Utilities.LogUtil import Logger

log = Logger(__name__,logging.INFO)

class Test_SignUp(BaseTest):

    @pytest.mark.parametrize("email,cemail,Fname,Lname, country, password,cpassword",
                             dataProvider.get_data("LoginTest"))
    def test_doSignUp(self, email,cemail,Fname,Lname, country, password,cpassword):
        log_message = "Test Do Sign up started"
        log.logger.info(log_message)
        allure.attach(log_message, name="Sign up Test Start", attachment_type=allure.attachment_type.TEXT)
        regPage = RegistrationPage(self.driver)
        regPage.fillForm(email,cemail,Fname,Lname, country, password,cpassword)
        log_message = "Test Do Sign up executed successfully"
        log.logger.info(log_message)
        allure.attach(log_message, name="Sign up Test Execution", attachment_type=allure.attachment_type.TEXT)
