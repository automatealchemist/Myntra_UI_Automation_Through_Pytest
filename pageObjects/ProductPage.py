import time
from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    #first_product = (By.XPATH, "//img[@title='//*[@id='22492582']/a/div[1]/div/div/div/picture/img")
    size_button = (By.XPATH, '//*[@id="sizeButtonsContainer"]/div[2]/div[2]/div[1]/button')
    add_to_bag_button = (By.XPATH, '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]')
    product_title = (By.XPATH, '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/h1[1]')
    product_price = (By.XPATH, '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/p[1]/span[1]/strong')

    def select_size(self):
        self.driver.find_element(*self.size_button).click()
        time.sleep(2)
        return self

    def add_to_bag(self):
        self.driver.find_element(*self.add_to_bag_button).click()
        time.sleep(3)
        return self

    def get_product_details(self):
        title = self.driver.find_element(*self.product_title).text
        price = self.driver.find_element(*self.product_price).text
        size = self.driver.find_element(*self.size_button).text

        product_details = {
            "title": title,
            "price": price,
            "size": size
        }

        print(f"Name of the product is: {title}")
        print(f"Price of the Product is: {price}")
        print(f"Size of the Product is: {size}")

        return product_details