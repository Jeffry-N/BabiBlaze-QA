import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.creds import *
from utilities.utils import AutomationLogger


def BlazeLogin(self, username, password):
    log = AutomationLogger.automation()
    email_locator = (By.XPATH, email)
    
    try:
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(email_locator)
        )
        log.info("Email element located")
    except TimeoutException:
        log.warning("Unable to locate email element in 60 seconds")
        raise

    self.driver.find_element(By.XPATH, email).send_keys(username)
    log.info("Sent username")
    
    self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    log.info("Sent password")
    
    self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/button').click()
    log.info("Clicked login button")

    dashboard_xpath = '/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div'
    try:
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, dashboard_xpath))
        )
        log.info("Dashboard element found – login successful")
    except TimeoutException:
        log.error("Dashboard element not found – login may have failed")
        raise
