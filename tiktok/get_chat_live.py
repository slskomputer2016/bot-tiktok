import os
import subprocess
from playwright.sync_api import sync_playwright
import time,os,random

url ="https://tiktok.com"

def jalankan_login_tiktok():
    user_data_dir = os.path.join(os.getcwd(), "chrome_profile4")
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir,
            executable_path=chrome_path,
            headless=False, 
            args=[
                "--disable-blink-features=AutomationControlled", 
                "--start-maximized" 
            ],
            no_viewport=True
        )
        
        page = context.new_page()
        print("Goto  TikTok...")
        page.goto(url, wait_until="load")
        print("\n" + "="*30)
        time.sleep(5)
        input("Please Enter ......")
        time.sleep(20)
        page.wait_for_timeout(3000)

        # names = page.locator('[data-e2e="message-owner-name"]')
        # print("Jumlah nama:", names.count())
        # for i in range(names.count()):
        # 	print("NAMA:", names.nth(i).inner_text())

        messages = page.locator('[data-e2e="chat-message"]')
        print("Jumlah chat:", messages.count())
        for i in range(messages.count()):
        	message = messages.nth(i)
        	name = message.locator('[data-e2e="message-owner-name"]' ).inner_text()
        	text = message.inner_text()
        	print(f"\n[{i + 1}]")
        	print("Nama :", name)
        	print("Chat :", text)




        #+--------------------------------------------------------------------+
        #+--------------------------------------------------------------------+
        #+--------------------------------------------------------------------+


        time.sleep(5)
        input("Please Enter ......")
        
        #+--------------------------------------------------------------------+
        #+--------------------------------------------------------------------+
        #+--------------------------------------------------------------------+
        context.close()

if __name__ == "__main__":
    jalankan_login_tiktok()
