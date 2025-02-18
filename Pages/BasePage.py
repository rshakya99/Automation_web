from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By  # Import By for locating elements
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import configReader
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        element = self.get_element(locator)
        element.click()
        log.logger.info(f"Clicking on an element: {locator}")

    def type_wait(self, locator, value):
        element = self.wait.until(EC.element_to_be_clickable(self.get_element(locator)))
        element.send_keys(value)
        log.logger.info(f"Typing on an element: {locator}")

    def type(self, locator, value):
        element = self.get_element(locator)
        element.send_keys(value)
        log.logger.info(f"Typing in an element: {locator}, value entered: {value}")

    def select(self, locator, value):
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(value)
        log.logger.info(f"Selecting from an element: {locator}, value selected: {value}")

    def moveTo(self, locator):
        element = self.get_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        log.logger.info(f"Moving to an element: {locator}")

    def get_element(self, locator):
        """Helper function to locate elements based on their locator type."""
        locator_type, locator_value = self.parse_locator(locator)
        return self.driver.find_element(locator_type, locator_value)

    def parse_locator(self, locator):
        """Parses locator strings and returns the corresponding By type and value."""
        locator_value = configReader.readConfig("locators", locator)
        if locator.endswith("_XPATH"):
            return By.XPATH, locator_value
        elif locator.endswith("_CSS"):
            return By.CSS_SELECTOR, locator_value
        elif locator.endswith("_ID"):
            return By.ID, locator_value
        else:
            raise ValueError(f"Invalid locator format: {locator}")
