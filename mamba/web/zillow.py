import os
import sys
import requests
from selenium import webdriver
from bs4 import BeautifulSoup


class ZillowRequest:

    ZWSID = "X1-ZWz19cpv0tdh57_46au6"

    def __init__(self,
                 street_number: int,
                 street_name: str,
                 city: str,
                 zipcode: int,
                 unit_number: int = None):
        driver = self.get_chrome_driver()
        driver.get('https://www.zillow.com')

    @staticmethod
    def get_chrome_driver():
        chromedriver = r"C:\Program Files (x86)\Google\chromedriver.exe"
        return webdriver.Chrome(chromedriver)
