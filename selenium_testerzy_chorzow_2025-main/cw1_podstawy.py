from selenium import webdriver
import time

# inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

url = "https://www.google.com"
new_url = "https://www.wp.pl"

# upobranie konkretnego adresu w przeglarce
driver.get(url)

# rozmiar okna
driver.maximize_window()
#driver.set_window_size(1600, 800)

# otwarcie drugiej zakładki
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)
driver.close()

#zatrzymanie skryptu
time.sleep(5)

# zamkniecie przegladarki
driver.quit()

# zamkniecie zakładki
#driver.close()