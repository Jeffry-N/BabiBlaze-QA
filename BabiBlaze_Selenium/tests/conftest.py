import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def Launchdriver(request):
    driver = webdriver.Firefox()
    driver.get("https://xpertbotacademy.online/nova/login")
    request.cls.driver = driver
    yield
    driver.quit()