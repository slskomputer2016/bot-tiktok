import os
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth

# ==========================================
# CONFIGURATION / KONFIGURASI
# ==========================================
PROXY_HOST = "http://191.96.254.138"  # Ganti dengan IP atau domain proxy
PROXY_PORT = 6185               # Ganti dengan port proxy
PROXY_USER = "gunawanred789"    # Ganti dengan username proxy
PROXY_PASS = "asephendra77"    # Ganti dengan password proxy


def create_proxy_auth_extension(proxy_host, proxy_port, proxy_user, proxy_pass):
    """Membuat ekstensi Chrome temporary untuk autentikasi proxy."""
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = f"""
    var config = {{
            mode: "fixed_servers",
            rules: {{
              singleProxy: {{
                scheme: "http",
                host: "{proxy_host}",
                port: parseInt({proxy_port})
              }},
              bypassList: []
            }}
          }};

    chrome.proxy.settings.set({{value: config, scope: "regular"}}, function({{}});

    chrome.webRequest.onAuthRequired.addListener(
            function(details) {{
                return {{
                    authCredentials: {{
                        username: "{proxy_user}",
                        password: "{proxy_pass}"
                    }}
                }};
            }},
            {{urls: ["<all_urls>"]}},
            ['blocking']
    );
    """
    
    plugin_file = 'proxy_auth_plugin.zip'
    with zipfile.ZipFile(plugin_file, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    
    return plugin_file


# ==========================================
# MAIN DRIVER SETUP
# ==========================================
options = webdriver.ChromeOptions()

# 1. Pasang Ekstensi Proxy Autentikasi
proxy_plugin_path = create_proxy_auth_extension(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
options.add_extension(proxy_plugin_path)

# 2. Pengaturan Chrome Options Standar untuk Stealth
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Inisialisasi Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 3. Terapkan Selenium Stealth
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True
        )

# ==========================================
# PENGUJIAN / TESTING
# ==========================================
try:
    # Cek apakah IP sudah berubah sesuai Proxy
    driver.get("https://httpbin.org")
    print("Response dari httpbin (Cek IP):")
    print(driver.find_element("tag name", "body").text)
    
    # Cek tingkat deteksi bot (Situs Pixelscan / Browserleak)
    driver.get("https://antcpt.com")
    print("\nSilakan cek jendela browser untuk melihat hasil deteksi bot.")
    
    input("Tekan Enter untuk menutup browser...")

finally:
    driver.quit()
    # Hapus file ekstensi temporary setelah selesai
    if os.path.exists(proxy_plugin_path):
        os.remove(proxy_plugin_path)
