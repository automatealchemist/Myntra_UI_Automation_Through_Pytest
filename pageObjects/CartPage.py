# This file contains the Page Object Model (POM) implementation for the Cart Detail Page.

import time

from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver


    cart_product_title = (By.XPATH, '//*[@id="cartItemsList"]/div/div/div/div[2]/div[2]/div/div[1]/div')
    cart_product_price = (By.XPATH, '//*[@id="cartItemsList"]/div/div/div/div[2]/div[2]/div/div[4]/div[1]/div')
    cart_product_size = (By.XPATH, '//*[@id="cartItemsList"]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/span')

    def get_cart_details(self):
        time.sleep(5)
        title = self.driver.find_element(*self.cart_product_title).text
        price = self.driver.find_element(*self.cart_product_price).text
        size = self.driver.find_element(*self.cart_product_size).text

        cart_details = {
            "title": title,
            "price": price,
            "size": size
        }

        print(f"Cart Product Title: {title}")
        print(f"Cart Product Price: {price}")
        print(f"Cart Product Size: {size}")

        return cart_details

