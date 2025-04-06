from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

url = "https://www.google.com"

# upobranie konkretnego adresu w przeglarce
driver.get(url)

# rozmiar okna
driver.maximize_window()

# lokalizacja przycisku, zeby zaakceptowac zgody
accept_cookies = driver.find_element("id", "L2AGLb")
accept_cookies.click()

# wprawadzenie hasla do wyszukania i szukanie
search_text = driver.find_element("name", "q")
search_text.send_keys("Pogoda")
search_text.send_keys(Keys.ENTER)
#search_text.submit()

#zatrzymanie skryptu
time.sleep(500)

# zamkniecie przegladarki
driver.quit()