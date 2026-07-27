import time
import json
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def setup_driver(prof):
    options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    #options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--disable-cache") 
    options.add_argument("--disable-blink-features=AutomationControlled")  
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument(r"user-data-dir="+prof)
    driver = webdriver.Chrome(options=options)
    return driver

def login(driver, email, password):
    #bot = tiktok_bot(driver)
    driver.get('https://www.tiktok.com/login/phone-or-email/email')

    # Input email and password using the bot
    type_text('//input[@type="text"]', email)
    time.sleep(1)
    type_text('//input[@type="password"]', password)
    time.sleep(1)

    start_url = driver.current_url

    # Submit login form
    click('//button[@type="submit"]')
    time.sleep(60)

def click(path):
    try:
        element = driver.find_element(By.XPATH, path)
        element.click()
    except Exception as e:
        print(f"Error clicking element: {e}")
def type_text(path, text):
    try:
        element = driver.find_element(By.XPATH, path)
        for char in text:
            element.send_keys(char)
            time.sleep(0.05)
    except Exception as e:
        print(f"Error typing text: {e}")

if __name__ == "__main__":

    profile= "D:/profiles/tiktok"
    driver = setup_driver(profile)
    login(driver,"aser@gmail.com","asepdhdh")