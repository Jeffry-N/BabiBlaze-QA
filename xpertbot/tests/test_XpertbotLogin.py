import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

def test_xpertbot_login():
    driver.get("https://xpertbotacademy.online/nova/login")

    driver.find_element(By.ID, "email").send_keys("bobweb@test.com")
    driver.find_element(By.ID, "password").send_keys("12345678")
    driver.find_element(By.XPATH, "/html/body/div/div/form/button").click()
    logedin_locator = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]")

    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located(logedin_locator))
    except TimeoutException as e:
        print(f"Login failed or took too long {e}")
        pytest.fail("Login failed or took too long")
        driver.quit()