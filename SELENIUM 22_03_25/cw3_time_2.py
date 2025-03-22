from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Inicjalizacja przeglądarki
driver = webdriver.Chrome()
driver.maximize_window()

# implicit wait
driver.implicitly_wait(5)

url = "https://www.w3schools.com/"

# Uruchomienie przeglądarki
driver.get(url)

# Akceptacja ciasteczek
accept_cookies = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "accept-choices"))
)
accept_cookies.click()

# Kliknięcie menu "Tutorials"
menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "navbtn_tutorials"))
)
ActionChains(driver).move_to_element(menu).click(menu).perform()

# Kliknięcie "Learn HTML"
learn_html = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[@title="HTML Tutorial"]'))
)
learn_html.click()

# Kliknięcie "HTML Input Types"
menuInput = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="leftmenuinnerinner"]/a[43]'))
)
ActionChains(driver).move_to_element(menuInput).click(menuInput).perform()

# Zatrzymanie skryptu
time.sleep(500)

# Zamknięcie przeglądarki
driver.quit()