import pytest
from selenium import webdriver

@pytest.fixture(scope="class") # scope class - runs before any class tests
def Launchdriver(request):
    driver = webdriver.Firefox()
    driver.get("https://xpertbotacademy.online/nova/login")
    request.cls.driver = driver
    yield # run the test then continue
    driver.quit()