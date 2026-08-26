import os
import subprocess
from playwright.sync_api import sync_playwright
import time,os,random

def jalankan_login_tiktok():
    # 1. Tentukan jalur data browser agar sesi Anda tersimpan aman
    user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    
    # Jalur standar Google Chrome di Windows
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    if not os.path.exists(chrome_path):
        # Jalur alternatif jika Windows Anda versi 32-bit atau instalasi kustom
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    print("Membuka Google Chrome asli dengan mode otomasi khusus...")
    
    with sync_playwright() as p:
        # 2. Luncurkan browser asli menggunakan launch_persistent_context
        # Metode ini membuang semua kode deteksi bot bawaan Playwright secara total
        context = p.chromium.launch_persistent_context(
            user_data_dir,
            executable_path=chrome_path,
            headless=False, # Wajib terlihat layar
            args=[
                "--disable-blink-features=AutomationControlled", # Hapus status otomatisasi
                "--start-maximized" # Buka layar penuh agar menyerupai manusia
            ],
            no_viewport=True
        )
        
        page = context.new_page()
        print("Membuka halaman login TikTok...")
        page.goto("https://tiktok.com", wait_until="load")
        
        print("\n" + "="*60)
        print(" Anda memiliki waktu 1 menit sebelum skrip ini selesai.")
        print("="*60 + "\n")
        time.sleep(80)

        #+--------------------------------------------------------------------+
        #+--------------------------------------------------------------------+
        #+--------------------------------------------------------------------+

        for i in range(700):
        	jeda_acak = random.uniform(0.2, 0.6)
        	time.sleep(jeda_acak)
        	try:
        		print("-"*50)
        		print(i)
        		tombol_berhasil_diklik = False
        		semua_frame = page.frames
        		#print(f"Ditemukan {len(semua_frame)} frame aktif di halaman ini.")
        		print("Ditemukan Frame")
        		for index, frame in enumerate(semua_frame):
        			try:
        				locator_tombol = frame.locator("[data-e2e='room-chat-like-btn']").first
        				if locator_tombol.count() > 0:
        					#print(f"-> Tombol ditemukan di Frame indeks ke-{index}!")
        					print("Step 1")
        					frame.evaluate("document.querySelector(\"[data-e2e='room-chat-like-btn']\").click()")
        					#print("==> BERHASIL KLIK TOMBOL LIKE VIA IFRAME! <==")
        					print("Step 2")
        					tombol_berhasil_diklik = True
        			except Exception:
        				continue

        		if not tombol_berhasil_diklik:
        			print("Tombol tidak ditemukan di frame manapun. Mencoba metode koordinat...")

        	except Exception as e:
        			print(f"Error pada sistem pemindaian frame: {e}")

        time.sleep(5)
        print("Perulangan ke 2 ....")
        for i in range(600):
        	jeda_acak = random.uniform(0.2, 0.6)
        	time.sleep(jeda_acak)
        	try:
        		print("-"*50)
        		print(i)
        		tombol_berhasil_diklik = False
        		semua_frame = page.frames
        		#print(f"Ditemukan {len(semua_frame)} frame aktif di halaman ini.")
        		print("Ditemukan Frame !!!")
        		for index, frame in enumerate(semua_frame):
        			try:
        				locator_tombol = frame.locator("[data-e2e='room-chat-like-btn']").first
        				if locator_tombol.count() > 0:
        					#print(f"-> Tombol ditemukan di Frame indeks ke-{index}!")
        					print("Step 1")
        					frame.evaluate("document.querySelector(\"[data-e2e='room-chat-like-btn']\").click()")
        					print("Step 2")
        					#print("==> BERHASIL KLIK TOMBOL LIKE VIA IFRAME! <==")
        					tombol_berhasil_diklik = True
        			except Exception:
        				continue

        		if not tombol_berhasil_diklik:
        			print("Tombol tidak ditemukan di frame manapun. Mencoba metode koordinat...")

        	except Exception as e:
        			print(f"Error pada sistem pemindaian frame: {e}")
        print("End Perulangan. ")
        time.sleep(30)
        context.close()
        #+--------------------------------------------------------------------+
        #+--------------------------------------------------------------------+
        #+--------------------------------------------------------------------+


if __name__ == "__main__":
    jalankan_login_tiktok()
