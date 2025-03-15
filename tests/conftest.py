import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    driver.maximize_window()
    driver.get("https://www.myntra.com")
    time.sleep(5)

    # Make driver available to the test class
    request.cls.driver = driver

    # Teardown
    yield
    driver.quit()