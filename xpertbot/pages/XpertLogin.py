import pytest
from selenium import webdriver
from time import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.functions import *

class Xpert6():
    def __init__(self, driver):
        self.driver = driver

    def XpertbotLogin(self, username, password): # page of xpertbotlogin
        XpertLogin(self, username, password)