from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def wait_fot_button(driver, element_id):
    # Definicja lokalizatora
    locator = ("id", element_id)
    # Tworzenie obiektu WebDriverWait
    wait = WebDriverWait(driver, 10, 0.5)
    # Czekanie na widoczność elementu
    return wait.until(EC.visibility_of_element_located(locator), "Element nie pojawił się po danym czasie")

# Inicjalizacja przeglądarki
driver = webdriver.Chrome()
url = "https://www.saucedemo.com/"

# Otwórz stronę
driver.get(url)

try:
    # Sprawdzenie, czy przycisk login jest widoczny
    login_button = wait_fot_button(driver, "login-button")

except TimeoutException:
    print("Element nie został znaleziony")

else:
    print("Element został znaleziony")

finally:
    # Zatrzymanie na 5 sekund i zamknięcie przeglądarki
    time.sleep(5)
    driver.quit()