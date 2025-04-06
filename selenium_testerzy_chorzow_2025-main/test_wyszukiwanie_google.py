import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # inicjalizacja przeglądarki Chrome
    driver = webdriver.Chrome()
    yield driver
    # zamkniecie przegladarki
    driver.quit()

# test
def test_google_search(driver):
    # otwarcie strony google.com
    # pobranie konkretnego adresu w przeglarce
    url = "https://www.google.com"
    driver.get(url)

    #sprawdzenie czy tytuł zakładki jest zgodny z oczekiwanym
    assert "Google" in driver.title

    # lokalizacja przycisku, zeby zaakceptowac zgody
    accept_cookies = driver.find_element(By.ID, "L2AGLb")
    accept_cookies.click()

    # wprawadzenie hasla do wyszukania i szukanie
    search_text = driver.find_element("name", "q")
    search_text.send_keys("Pogoda")
    search_text.send_keys(Keys.ENTER)
    #search_text.submit()

    time.sleep(20)

    # sprawdzenie, czy wyniki wyslwietlily sie na stronie
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    #print("dlugosc listy: ", str(len(results)))
    assert len(results) > 0, "Niestety, nic nie ma"

    #zatrzymanie skryptu
    #time.sleep(500)