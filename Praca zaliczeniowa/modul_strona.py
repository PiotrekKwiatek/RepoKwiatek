import asyncio
from playwright.async_api import async_playwright, TimeoutError

async def odpalanie_strony(p):
    browser = await p.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://mapy.com/pl/")

    try:
        # Czekaj max 5 sekund na przycisk zgody na cookies
        await page.wait_for_selector('button[data-testid="button-agree"]', timeout=5000)
        await page.click('button[data-testid="button-agree"]')
        await page.wait_for_timeout(1000)
        print("Przycisk cookies został kliknięty i zniknął")
    except TimeoutError:
        # Jeśli przycisk się nie pojawił, pomiń
        print("Przycisk cookies nie był widoczny, pomijam")

    try:
        strona = await page.wait_for_selector('//*[@id="mapycz"]', timeout=5000)
        if await strona.is_visible():
            print("Strona jest widoczna")
        else:
            print("Strona się nie załadowała")
    except TimeoutError:
        print("Nie udało się znaleźć elementu z mapą")

    return browser, page
