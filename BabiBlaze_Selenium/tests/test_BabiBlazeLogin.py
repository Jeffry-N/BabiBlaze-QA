import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utilities.utils import AutomationLogger
from pages.BlazeLogin import Blaze1
from pages.creds import username, password, email

log = AutomationLogger.automation()


@pytest.mark.usefixtures("Launchdriver")
class TestBlazeLogin:

    def test_login(self):
        try:
            log.info("Test has started")

            Blaze = Blaze1(self.driver)
            Blaze.BlazeAdminLogin(username=username, password=password)

            log.info("Login function executed successfully")

        except Exception as e:
            log.error(f"An error occurred: {e}")
            raise
