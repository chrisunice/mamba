import os
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ZillowRequest:

    ZWSID = "X1-ZWz19cpv0tdh57_46au6"

    def __init__(self,
                 street_number: int,
                 street_name: str,
                 city: str,
                 zipcode: int,
                 unit_number: int = None):
        driver = self.get_chrome_driver()
        driver.get("https://www.zillow.com")
        driver.implicitly_wait(10)
        search_bar = driver.find_element(By.ID, "search-box-input")
        search_bar.send_keys("2769 Brands Hatch Court Henderson NV 89052")
        driver.close()

    @staticmethod
    def get_chrome_driver():
        chromedriver = r"C:\Program Files (x86)\Google\chromedriver.exe"
        return webdriver.Chrome(chromedriver)

