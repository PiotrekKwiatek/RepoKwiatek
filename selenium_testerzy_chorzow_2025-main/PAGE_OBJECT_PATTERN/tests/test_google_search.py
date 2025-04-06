import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pytest
import time
from PAGE_OBJECT_PATTERN.google_search import SearchPage
from PAGE_OBJECT_PATTERN.google_results import ResultPage
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    

# test
def test_google_serach(driver):
    search_page = SearchPage(driver)
    search_page.open()

    assert "Google" in driver.title

    search_page.accept_cookies()

    search_page.search("Pogoda")

    time.sleep(20)

    result_page = ResultsPage(driver)
    results = result_page.get_results()

    assert len(results) > 0, "No results found"
