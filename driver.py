import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def driver():
    service = Service(executable_path=r'C:\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    return driver