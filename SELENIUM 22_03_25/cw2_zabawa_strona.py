from selenium import webdriver
from selenium.webdriver.common.by import By  # Import klasy By
import time

# inicjalizacja przeglądarki
driver = webdriver.Chrome()

url = "https://www.google.com"

# uruchomienie przeglądarki z podanym adresem
driver.get(url)

# rozmiar okna
driver.maximize_window()

# kliknięcie przycisku zaakceptuj wszystko
accept_cookies = driver.find_element(By.ID, "L2AGLb")  
accept_cookies.click()

#wprowadzenie hasła do wyszukiwarki
search_text = driver.find_element(By.NAME, "q")  
search_text.send_keys("Pogoda w Jeleniej Górze")

#wcisniecie enter
search_text.submit()

# zatrzymanie skryptu
time.sleep(100)

# zamknięcie zakładki
driver.quit()

