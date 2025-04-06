class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.accept_cookies_button = ("id", "L2AGLb")
        self.search_textbox = ("name", "q")

    def open(self):
        self.driver.get("https://www.google.com")

    def accept_cookies(self):
        accept_cookies = self.driver.find_element(*self.accept_cookies_button)
        accept_cookies.click()

    def search(self, query):
        search_textbox = self.driver.find_element(*self.search_textbox)
        search_textbox.send_keys(query)
        search_textbox.submit(Keys.ENTER)