#This file contains the Page Object Model (POM) implementation for the Product Detail Page.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage:
    # Locators
    SIZE_BUTTON_LOCATOR = (By.XPATH, '//*[@id="sizeButtonsContainer"]/div[2]/div[2]/div[1]/button')
    ADD_TO_BAG_BUTTON_LOCATOR = (By.XPATH, '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]')
    PRODUCT_TITLE_LOCATOR = (By.XPATH, '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/h1[1]')
    PRODUCT_PRICE_LOCATOR = (By.XPATH, '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/p[1]/span[1]/strong')
    CART_ICON_LOCATOR = (By.XPATH, '//*[@id="desktop-header-cnt"]/div[2]/div[2]/a[2]/span[1]')
    BLOCK_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Block']")
    NAVIGATE_TO_CART_PAGE = (By.XPATH, '//*[@id="desktop-header-cnt"]/div[2]/div[2]/a[2]/span[1]')
    TSHIRT_TITLE = (By.XPATH,'//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/h1[1]')
    TSHIRT_PRICE = (By.XPATH,'//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/p[1]/span[1]/strong')
    TSHIRT_SIZE = (By.XPATH, '//*[@id="sizeButtonsContainer"]/div[2]/div[2]/div[1]/button')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def handle_notification_popup(self):

        try:

            wait = WebDriverWait(self.driver, 5)  # Wait up to 5 seconds
            block_button = wait.until(EC.element_to_be_clickable(self.BLOCK_BUTTON_LOCATOR))
            # Click the "Block" button
            block_button.click()
            print("Notification blocked.")
        except:

            print("No notification pop-up appeared.")

    def handle_window_switching(self):

        windowIDs = self.driver.window_handles
        for windowID in windowIDs:
            self.driver.switch_to.window(windowID)
            print(self.driver.title)

    def select_size(self):

        self.driver.find_element(*self.SIZE_BUTTON_LOCATOR).click()
        time.sleep(2)

    def add_to_bag(self):
        self.driver.find_element(*self.ADD_TO_BAG_BUTTON_LOCATOR).click()
        time.sleep(3)

    def get_product_details(self):

        title = self.driver.find_element(*ProductPage.TSHIRT_TITLE).text
        price = self.driver.find_element(*ProductPage.TSHIRT_PRICE).text
        size = self.driver.find_element(*ProductPage.TSHIRT_SIZE).text

        product_details = {
            "title": title,
            "price": price,
            "size": size
        }

        print(f"Product Name: {title}")
        print(f"Product Price: {price}")
        print(f"Product size: {size}")
        return product_details

    def navigate_to_cart(self):

        cart_button = self.driver.find_element(*ProductPage.NAVIGATE_TO_CART_PAGE)
        cart_button.click()
        time.sleep(3)
        print("Navigated to cart page.")

    def go_to_cart(self):

        self.driver.find_element(*self.CART_ICON_LOCATOR).click()
        time.sleep(3)

