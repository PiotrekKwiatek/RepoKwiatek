from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicjalizacja przeglądarki
driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.w3schools.com/"
driver.get(url)

# Akceptacja ciasteczek
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "accept-choices"))
).click()

# Kliknięcie menu "Tutorials"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "navbtn_tutorials"))
).click()

# Kliknięcie "Learn HTML"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="tutorials_html_css_links_list"]/div[1]/a[1]'))
).click()

# Kliknięcie "Tag List"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="leftmenuinnerinner"]/a[71]'))
).click()

# Kliknięcie "Input"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="leftmenuinnerinner"]/div/a[59]'))
).click()

# Kliknięcie "Disable"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/table[2]/tbody/tr[8]/td[1]/a'))
).click()

# Kliknięcie "Try it yourself"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[2]/a'))
).click()

# Przełączenie na nową zakładkę
currentWindow = driver.current_window_handle
windowsNames = driver.window_handles
print(f"Obecne zakładki: {windowsNames}")

for window in windowsNames:
    if window != currentWindow:
        driver.switch_to.window(window)
        print(f"Przełączono na zakładkę: {window}")

# Przełączenie do iframe
try:
    iframe = driver.find_element(By.ID, 'iframeResult')
    print("Iframe znaleziony!")
    driver.switch_to.frame(iframe)
except Exception as e:
    print(f"Błąd: {e}")

# Wprowadzenie imienia
try:
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'fname'))
    )
    print("Element 'fname' znaleziony!")
    name_input.send_keys("Piotr")
except Exception as e:
    print(f"Błąd: {e}")


time.sleep(500)

# Zamknięcie przeglądarki
driver.quit()



