import pytest
from selenium.webdriver import ActionChains
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHomePage(BaseClass):
    def test_navigation_to_tshirts(self):
        homepage = HomePage(self.driver)

        # Handle notification if appears
        self.handle_notification_popup()

        # Create action chains instance for hover
        action = ActionChains(self.driver)

        # Navigate to T-shirts section
        homepage.hover_on_men_menu(action)
        homepage.click_casual_tshirts()

        assert "Casual T-shirts" in self.driver.title, "Navigation to T-shirts page failed"