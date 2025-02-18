from time import sleep

import pytest

from Pages.LoginPage import LoginPage
from Pages.RegistrationPage import RegistrationPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider

import logging
import pytest
import allure
from time import sleep
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class Test_login(BaseTest):

    @pytest.mark.parametrize("email, password",
                             dataProvider.get_data("LoginTest1"))
    def test_dologin(self, email, password):
        log_message = "Test Do Login started"
        log.logger.info(log_message)
        allure.attach(log_message, name="Login Test Start", attachment_type=allure.attachment_type.TEXT)

        regPage = LoginPage(self.driver)
        regPage.fill_login(email, password)

        log_message = "Test Do Login executed successfully"
        log.logger.info(log_message)
        allure.attach(log_message, name="Login Test Execution", attachment_type=allure.attachment_type.TEXT)

        sleep(15)
