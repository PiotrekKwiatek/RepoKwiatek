from selenium import webdriver
from selenium.webdriver.common.by import By  # Import klasy By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# inicjalizacja przeglądarki
driver = webdriver.Chrome()
driver.maximize_window()

#implicit wait
driver.implicitly_wait(5)

url = "https://www.w3schools.com/"

# uruchomienie przeglądarki z podanym adresem
driver.get(url)

accept_cookies = driver.find_element(By.ID, "accept-choices")
accept_cookies.click()


menu = driver.find_element(By.ID, "navbtn_tutorials") 
#menu.click()
webdriver.ActionChains(driver).move_to_element(menu).click(menu).perform()

# zatrzymanie skryptu
time.sleep(500)

# zamknięcie zakładki
driver.quit()