from selenium import webdriver
import time

#inicjalizacja przeglądarki
driver = webdriver.Chrome()

url = "https://www.google.com"
new_url = "https://www.wp.pl"   

#urchumienie przeglądarki z podanym adresem
driver.get(url)

#rozmiar okna
driver.maximize_window()
#driver.set_window_size(1600,800)

#otwarcie drugiej zakładki
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)

#zatrzymanie skryptu
time.sleep(5)

driver.close()

#zatrzymanie skryptu
time.sleep(2)

#zamknięcie przeglądarki
#driver.quit()

#zamkniecie zakładki
driver.quit()