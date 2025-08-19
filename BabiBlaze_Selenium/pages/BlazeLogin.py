import pytest
from selenium import webdriver
from time import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.functions import *

class Blaze():
    def __init__(self, driver):
        self.driver = driver

    def BlazeAdminLogin(self, username, password):
        BlazeLogin(self, username, password)