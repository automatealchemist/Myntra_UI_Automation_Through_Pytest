import pytest
from utilities.BaseClass import BaseClass
from pageObjects.ProductPage import ProductPage


class TestProductPage(BaseClass):
    def test_add_product_to_bag(self):
        product_page = ProductPage(self.driver)

        # Click on first product
        #product_page.click_first_product()

        # Switch to new window
        self.switch_to_window_with_title()

        # Handle notification if appears
        self.handle_notification_popup()

        # Select size and add to bag
        product_page.select_size()
        product_details = product_page.get_product_details()
        product_page.add_to_bag()

        # Verify product details
        assert product_details["title"] != "", "Product title is empty"
        assert product_details["price"] != "", "Product price is empty"
        assert product_details["size"] != "", "Product size is empty"

        return product_details