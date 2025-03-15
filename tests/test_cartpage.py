import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CartPage import CartPage


class TestCartPage(BaseClass):
    def test_verify_cart_details(self, product_details=None):
        homepage = HomePage(self.driver)
        cart_page = CartPage(self.driver)

        # Go to cart
        homepage.go_to_cart()

        # Get cart details
        cart_details = cart_page.get_cart_details()

        # Verify cart details
        assert cart_details["title"] != "", "Cart product title is empty"
        assert cart_details["price"] != "", "Cart product price is empty"
        assert cart_details["size"] != "", "Cart product size is empty"

        # If product details are provided, verify they match cart details
        if product_details:
            assert product_details["title"] == cart_details["title"], "Product title doesn't match with cart"
            assert product_details["price"] == cart_details["price"], "Product price doesn't match with cart"
            assert product_details["size"] == cart_details["size"], "Product size doesn't match with cart"

        return cart_details