import pytest
from selenium.webdriver import ActionChains
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from pageObjects.CartPage import CartPage
import re

class TestEndToEnd(BaseClass):
    def test_myntra_shopping_flow(self):
        # Initialize page objects
        homepage = HomePage(self.driver)
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)

        # Handle notification if appears
        self.handle_notification_popup()

        # Create action chains instance for hover
        action = ActionChains(self.driver)

        # Step 1: Navigate to Men's T-shirts section
        homepage.hover_on_men_menu(action)
        homepage.click_casual_tshirts()

        # Step 2: Select the first product - CHANGE THIS LINE
        # From: product_page.click_first_product()
        # To: homepage.click_first_product()
        homepage.click_first_product()  # Change this line in your test

        # Switch to new window
        self.switch_to_window_with_title()

        # Handle notification if appears
        self.handle_notification_popup()

        # Step 3: Select size and add to bag
        product_page.select_size()
        product_details = product_page.get_product_details()
        product_page.add_to_bag()

        # Step 4: Go to cart and verify details
        homepage.go_to_cart()
        cart_details = cart_page.get_cart_details()
        item_price = product_details["price"].strip("₹")
        cart_price = cart_details["price"] # your string here


        cart_price = re.sub(',','', cart_price)
        cart_size = cart_details["size"].strip("Size: ")

        if product_details["title"]== cart_details["title"]:
            print("T-shirt title matched.")
        else:
            print("Title doesnot matched.")
        if item_price== cart_price:
            print("T-shirt price matched.")
        else:
            print("Price doesnot matched.")
        if product_details["size"]== cart_size:
            print("T-shirt size matched.")
        else:
            print("Size doesnot matched.")


