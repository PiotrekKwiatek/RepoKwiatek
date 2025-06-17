import asyncio
from modul_strona import odpalanie_strony
from playwright.async_api import async_playwright

WIDOKI = {
    "turisticka": "turystyczna",
    "letecka": "lotnicza",
    "dopravni": "drogowa",
    "zimni": "zimowa",
    "zakladni": "podstawowa",
}

async def test_przelaczanie_widokow(page):
    await page.wait_for_selector('mapy-map-toggle.map-controls__mapset')
    await page.click('mapy-map-toggle.map-controls__mapset')

    wszystkie_dzialaja = True

    for url_fragment, polska_nazwa in WIDOKI.items():
        try:
            await page.wait_for_selector(f'img[src*="{url_fragment}-small.png"]', timeout=5000)
            await page.click(f'img[src*="{url_fragment}-small.png"]')
            await page.wait_for_timeout(1000)

            current_url = page.url
            if url_fragment in current_url:
                print(f"Mapa {polska_nazwa} włącza się prawidłowo")
            else:
                print(f"Mapa {polska_nazwa} nie włączyła się poprawnie (URL: {current_url})")
                wszystkie_dzialaja = False
        except Exception as e:
            print(f"Błąd przy włączaniu widoku '{polska_nazwa}': {e}")
            wszystkie_dzialaja = False

    if wszystkie_dzialaja:
        print("Przełączanie wszystkich widoków mapy działa prawidłowo")
    else:
        print("Nie wszystkie testy przeszły poprawnie")

async def main():
    async with async_playwright() as p:
        browser, page = await odpalanie_strony(p)
        try:
            print("Test bazowy przeszedł, uruchamiam test przełączania widoków")
            await test_przelaczanie_widokow(page)
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
