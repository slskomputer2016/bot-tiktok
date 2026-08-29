from playwright.sync_api import sync_playwright
from pathlib import Path
import time,random,os,re
from datetime import datetime



profile ="fitsa2016"
URL = "https://ads.tiktok.com/business/creativecenter"
PROFILE_DIR = Path(f"profiles/{profile}")
def close_popup(page):
    selectors = [
        'button[aria-label="Close"]',
        'button[aria-label="close"]',
        '[data-testid="modal-close"]',
        '[data-testid="close"]',
        'button:has-text("Close")',
        'button:has-text("Got it")',
        'button:has-text("Not now")',
        '[role="dialog"] button',
    ]

    for selector in selectors:
        try:
            locator = page.locator(selector)

            if locator.count() > 0:
                for i in range(locator.count()):
                    try:
                        if locator.nth(i).is_visible():
                            locator.nth(i).click()
                            print("Popup ditutup:", selector)
                            return True
                    except:
                        pass

        except:
            pass

    return False

def main():
    with sync_playwright() as p:

        PROFILE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        print("=" * 60)
        print("TIKTOK CREATIVE CENTER")
        print("=" * 60)

        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            channel="chrome",
            headless=False,
            no_viewport=True,
            args=[
                "--disable-blink-features=AutomationControlled", 
                "--start-maximized"
            ]
        )

        if browser.pages:
            page = browser.pages[0]
        else:
            page = browser.new_page()

        # Tutup tab lain
        for extra_page in browser.pages:
            if extra_page != page:
                try:
                    extra_page.close()
                except Exception:
                    pass

        try:

            # =================================================
            # 1. BUKA CREATIVE CENTER
            # =================================================

            print()
            print("Membuka Creative Center...")

            page.goto(
                URL,
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(10000)
            #input("Enter untuk melanjutkan ...... ")
            print()
            print("URL awal:")
            print(page.url)
            # page.screenshot(
            #     path="01_awal.png",
            #     full_page=True
            # )
            time.sleep(5)
            close_popup(page)

            # =================================================
            # 2. KLIK TRENDS
            # =================================================
            print()
            print("-" * 60)
            print("Mencari menu Trends...")
            print("-" * 60)
            trends = page.get_by_text(
                "Trends",
                exact=True
            )
            jumlah_trends = trends.count()
            print(
                "Jumlah Trends:",
                jumlah_trends
            )
            trends_clicked = False
            for i in range(jumlah_trends):
                try:
                    item = trends.nth(i)
                    if not item.is_visible():
                        continue
                    print(
                        f"Klik Trends index {i}"
                    )
                    item.scroll_into_view_if_needed()
                    page.wait_for_timeout(500)
                    item.click(
                        force=True
                    )
                    trends_clicked = True
                    break
                except Exception as e:

                    print(
                        "Gagal klik Trends:",
                        e
                    )

            if not trends_clicked:

                print()
                print(
                    "ERROR: Trends tidak berhasil diklik."
                )

                input(
                    "\nENTER untuk menutup..."
                )

                return

            print()
            print(
                "Trends berhasil diklik."
            )

            # =================================================
            # 3. TUNGGU HALAMAN TRENDS
            # =================================================

            page.wait_for_timeout(5000)
            print()
            print(
                "URL setelah Trends:"
            )

            print(
                page.url
            )

            page.screenshot(
                path="02_trends.png",
                full_page=True
            )

            # =================================================
            # 4. CARI REGION USA
            # =================================================

            print()
            print("-" * 60)
            print("MENCARI REGION")
            print("-" * 60)

            usa = page.get_by_text(
                "United States of America",
                exact=True
            )

            jumlah_usa = usa.count()

            print(
                "Jumlah United States of America:",
                jumlah_usa
            )

            if jumlah_usa == 0:

                print()
                print(
                    "❌ United States of America tidak ditemukan."
                )

                page.screenshot(
                    path="03_region_tidak_ditemukan.png",
                    full_page=True
                )

                input(
                    "\nENTER untuk menutup..."
                )

                return

            # =================================================
            # 5. KLIK USA YANG VISIBLE
            # =================================================

            usa_clicked = False

            for i in range(jumlah_usa):
                try:
                    item = usa.nth(i)
                    visible = item.is_visible()
                    print(
                        f"USA index {i} | visible = {visible}"
                    )
                    if not visible:
                        continue
                    print()
                    print(
                        "Klik United States of America..."
                    )
                    item.scroll_into_view_if_needed()
                    page.wait_for_timeout(500)
                    item.click(
                        force=True
                    )
                    usa_clicked = True
                    print(
                        "✅ USA berhasil diklik."
                    )
                    break
                except Exception as e:
                    print(
                        "Gagal klik USA:",
                        e
                    )
            if not usa_clicked:
                print()
                print(
                    "❌ Tidak berhasil klik USA."
                )
                input(
                    "\nENTER untuk menutup..."
                )
                return

            # =================================================
            # 6. TUNGGU DROPDOWN
            # =================================================
            print()
            print(
                "Menunggu dropdown region..."
            )
            page.wait_for_timeout(1500)
            page.screenshot(
                path="03_dropdown_region.png",
                full_page=True
            )
            # =================================================
            # 7. CARI INDONESIA
            # =================================================
            print()
            print("-" * 60)
            print("MENCARI INDONESIA DI DROPDOWN")
            print("-" * 60)
            indonesia = page.get_by_text(
                "Indonesia",
                exact=True
            )
            jumlah_indonesia = indonesia.count()
            print(
                "Jumlah Indonesia:",
                jumlah_indonesia
            )
            if jumlah_indonesia == 0:
                print()
                print(
                    "❌ Indonesia belum ditemukan."
                )
                print()
                print(
                    "Dropdown mungkin belum terbuka."
                )
                page.screenshot(
                    path="04_indonesia_tidak_ditemukan.png",
                    full_page=True
                )
                input(
                    "\nENTER untuk menutup..."
                )
                return

            # =================================================
            # 8. KLIK OPTION INDONESIA
            # =================================================

            indonesia_clicked = False

            for i in range(jumlah_indonesia):

                try:

                    item = indonesia.nth(i)

                    visible = item.is_visible()

                    print(
                        f"Indonesia index {i} | visible = {visible}"
                    )

                    if not visible:
                        continue

                    print()
                    print(
                        "Klik Indonesia..."
                    )

                    item.scroll_into_view_if_needed()

                    page.wait_for_timeout(300)

                    item.click(
                        force=True
                    )

                    indonesia_clicked = True

                    print(
                        "✅ Indonesia berhasil diklik."
                    )

                    break

                except Exception as e:

                    print(
                        "Gagal klik Indonesia:",
                        e
                    )

            if not indonesia_clicked:

                print()
                print(
                    "❌ Indonesia tidak berhasil diklik."
                )

                input(
                    "\nENTER untuk menutup..."
                )

                return

            # =================================================
            # 9. TUNGGU REGION BERUBAH
            # =================================================

            print()
            print(
                "Menunggu region berubah..."
            )

            page.wait_for_timeout(5000)

            print()
            print(
                "URL setelah memilih Indonesia:"
            )

            print(
                page.url
            )

            page.screenshot(path="04_indonesia.png",full_page=True)

            # =================================================
            # 10. CEK REGION
            # =================================================

            print()
            print("-" * 60)
            print("MEMERIKSA REGION")
            print("-" * 60)

            body_text = page.locator(
                "body"
            ).inner_text()

            if "Browse what's trending now in Indonesia" in body_text:

                print()
                print(
                    "🎉 REGION INDONESIA BERHASIL!"
                )

            elif "Indonesia" in body_text:

                print()
                print(
                    "⚠️ Indonesia ditemukan di halaman."
                )

            else:
                print()
                print(
                    "❌ Indonesia belum terdeteksi."
                )




            # =================================================
            # 11. TAMPILKAN URL DAN TEKS REGION
            # =================================================

            print()
            print(
                "URL:"
            )

            print(
                page.url
            )

            print()
            print(
                "Mencari teks region..."
            )

            lines = body_text.splitlines()

            for i, line in enumerate(lines):

                line = line.strip()

                if "Indonesia" in line:

                    print(
                        f"{i}: {line}"
                    )

            # =================================================
            # 12. SIMPAN TEXT
            # =================================================

            with open(
                "indonesia_text.txt",
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    body_text
                )
            print()
            print("Text disimpan:")
            print("indonesia_text.txt")
            # =================================================
            # 13. BERHENTI
            # =================================================
            print()
            print("=" * 60)
            print("TAHAP REGION SELESAI")
            print("=" * 60)


            time.sleep(2)
            #page.pause()
            #hashtag = page.get_by_text("#gangstarmiragecity",exact=True)
            page.evaluate("window.scrollTo(0, 1200)")
            time.sleep(3)
            waktu = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            page.screenshot(path=f"hashtag_{waktu}.png",full_page=True)

            # await page.evaluate(() => {
            #     window.scrollTo({top: 100,behavior: 'smooth'});
            # });



            #input("Enter untuk melanjutkan ...... ")
            time.sleep(4)
            hashtag = page.get_by_text(re.compile(r"^#.+$"),exact=True).first


            container = hashtag.first.locator("xpath=ancestor::div[3]")
            rows = container.locator(":scope > div")
            data = []
            for i in range(rows.count()):
                row = rows.nth(i)
                item = parse_row(row)
                data.append(item)


            for item in data:
                print(
                    f"{item['rank']:>3} | "
                    f"{item['hashtag']:<30} | "
                    f"{item['category']:<25} | "
                    f"{item['views']}")

















            # hashtag = page.get_by_text("#gangstarmiragecity",exact=True)
            # print("Hashtag ditemukan:", hashtag.count())
            # if hashtag.count() > 0:
            #     container = hashtag.first.locator("xpath=ancestor::div[3]")
            #     print("=" * 80)
            #     print("CONTAINER LEVEL 3")
            #     print(container.inner_text())
            #     children = container.locator(":scope > div")
            #     print("\nJumlah child langsung:", children.count())
            #     for i in range(children.count()):
            #         print("\n" + "-" * 80)
            #         print("CHILD:", i)
            #         print(children.nth(i).inner_text())





            # hashtag = page.get_by_text("#gangstarmiragecity",exact=True).first
            # print("Hashtag ditemukan:", hashtag.count())
            # if hashtag.count() > 0:
            #     for level in range(1, 8):
            #         try:
            #             locator = hashtag.locator(f"xpath=ancestor::*[{level}]")
            #             text = locator.inner_text()
            #             print("\n" + "=" * 80)
            #             print("LEVEL:", level)
            #             print("=" * 80)
            #             print(text)

            #         except Exception as e:
            #             print("ERROR:", e)




            #page.get_by_role("link", name="Video Video Find inspiration").click()
            #page.pause()
            # input(
            #     "\nENTER untuk menutup browser..."
            # )























        except Exception as e:
            print()
            print("=" * 60)
            print("ERROR")
            print("=" * 60)
            print(type(e).__name__)
            print(e)
            try:
                page.screenshot(
                    path="error.png",
                    full_page=True
                )
            except Exception:
                pass
            input("\nENTER untuk menutup browser...")

        finally:

            browser.close()


def parse_row(row):

    lines = [
        x.strip()
        for x in row.inner_text().split("\n")
        if x.strip()
    ]

    result = {
        "rank": "",
        "hashtag": "",
        "category": "",
        "posts": "",
        "views": ""
    }

    # -------------------------
    # Rank
    # -------------------------
    if lines and lines[0].isdigit():
        result["rank"] = int(lines[0])

    # -------------------------
    # Hashtag
    # -------------------------
    hashtag_index = None

    for i, text in enumerate(lines):

        if text.startswith("#"):
            result["hashtag"] = text
            hashtag_index = i
            break

    # -------------------------
    # Category
    # -------------------------
    if hashtag_index is not None:

        next_index = hashtag_index + 1

        if next_index < len(lines):

            value = lines[next_index]

            # Kalau bukan angka Posts/Views
            if (
                value not in ["Posts", "Views", "See analytics"]
                and not value.endswith("K")
                and not value.endswith("M")
                and not value.endswith("B")
            ):
                result["category"] = value

    # -------------------------
    # Posts
    # -------------------------
    for i, text in enumerate(lines):

        if text == "Posts" and i > 0:
            result["posts"] = lines[i - 1]

    # -------------------------
    # Views
    # -------------------------
    for i, text in enumerate(lines):

        if text == "Views" and i > 0:
            result["views"] = lines[i - 1]

    return result


if __name__ == "__main__":
    main()
