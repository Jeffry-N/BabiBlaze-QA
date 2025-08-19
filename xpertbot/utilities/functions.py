import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.creds import *
from utilities.utils import AutomationLogger


def XpertLogin(self,username,password):
    log=AutomationLogger.automation()
    email_locator= (By.XPATH,email)
    log.info("Location email")
    try:
        WebDriverWait(self.driver,60).until(
            EC.presence_of_element_located(email_locator)
        )
    except NoSuchElementException as e:
        self.log.warning("unable to locate element")
        self.driver.find_element(By.XPATH,email).send_keys(username)
        log.info("Sent username")
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div/div/form/button').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="nova"]/div/div[2]/div[1]/div[2]/div/button/div').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT,'Logout').click()
        time.sleep(3)