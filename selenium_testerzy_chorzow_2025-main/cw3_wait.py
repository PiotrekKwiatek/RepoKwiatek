from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

# implicitly wait - oczekiwanie na pojawie się każdego elementu na stronie przez maksymanie X (podajemy jako parametr) sekund
# driver.implicitly_wait(5)

url = "https://www.w3schools.com/"

# upobranie konkretnego adresu w przeglarce
driver.get(url)

# rozmiar okna
driver.maximize_window()

# ciasteczka
time.sleep(5)
accept_cookies2 = driver.find_element("id", "accept-choices")
accept_cookies2.click()
# driver.find_element("id", "accept-choices").click()

# Tutorials
menu = driver.find_element("id", "navbtn_tutorials")
menu.click()
#webdriver.ActionChains(driver).move_to_element(menu).click().perform()

# learn HTML
learnHTML = driver.find_element('xpath', '//*[@id="tutorials_html_css_links_list"]/div[1]/a[1]')
#learnHTML = driver.find_element('xpath', '//a[@title="HTML Tutorial"]')
learnHTML.click()

# explicitly wait - czekamy na konketny element
wait = WebDriverWait(driver,10,0.5)
# warunek oczekiwania
wait.until(EC.visibility_of_element_located(('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')))
# gdyby był problem, to można uzyc starej metody
# wait.until(EC.visibility_of_element_located((By.XPATH , '//*[@id="leftmenuinnerinner"]/a[43]')))
# wait.until(lambda x: len(x.find_elements('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')))

# menu 'input types'
menuInput = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')
menuInput.click()

#zatrzymanie skryptu
time.sleep(500)

# zamkniecie przegladarki
driver.quit()