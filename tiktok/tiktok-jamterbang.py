import time,datetime,os,random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            item = [line.strip() for line in file if line.strip()]
        if not item:
            print("No item found in the file.")
            return []
        return item
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def setup_driver(prof):
    options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    #options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--disable-cache") 
    options.add_argument("--disable-blink-features=AutomationControlled")  
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("detach", True)
    options.add_argument(r"user-data-dir="+prof)
    driver = webdriver.Chrome(options=options)
    return driver



def daftar_tiktok(driver):
    while True:
        #driver.get("https://www.tiktok.com/login/phone-or-email/email")
        driver.get("https://www.tiktok.com")
        time.sleep(5)
        for i in range(7):
            btn = driver.find_element(By.XPATH, "//*[@id='main-content-homepage_hot']/aside/div/div[2]/button")
            time.sleep(5)
            btn.click()
            time.sleep(random.randint(30,112))
            print("Next video .... ")
            print("")



if __name__ == "__main__":
    prof = load_file("./files/email-tiktok.txt")
    for email in prof:
        os.system('cls' if os.name == 'nt' else 'clear')
        p = f"D:/profiles/tiktok/{email}"
        driver = setup_driver(p)
        daftar_tiktok(driver)
        driver.quit()
        time.sleep(2)



