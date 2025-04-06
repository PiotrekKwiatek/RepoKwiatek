from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.result = (By.CSS_SELECTOR, 'h3')

    def get_result(self):
        return self.driver.find_elements(*self.result)