import pytest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_link_presence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def handle_notification_popup(self):
        try:
            wait = WebDriverWait(self.driver, 5)  # Wait up to 5 seconds
            block_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Block']")))
            # Click the "Block" button
            block_button.click()
            print("Notification blocked.")
        except:
            # If pop-up does not appear, continue with execution
            print("No notification pop-up appeared.")

    def hover_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def switch_to_window_with_title(self, expected_title=None):
        window_ids = self.driver.window_handles
        for window_id in window_ids:
            self.driver.switch_to.window(window_id)
            print(f"Window title: {self.driver.title}")
            if expected_title and expected_title in self.driver.title:
                return True
        return False if expected_title else None