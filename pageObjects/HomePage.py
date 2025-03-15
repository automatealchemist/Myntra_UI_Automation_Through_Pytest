import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    men_link = (By.LINK_TEXT, 'MEN')
    casual_tshirt_link = (
    By.XPATH, '//*[@id="desktop-header-cnt"]/div[2]/nav/div/div[1]/div/div/div/div/li[1]/ul/li[2]/a')
    cart_icon = (By.XPATH, '//*[@id="desktop-header-cnt"]/div[2]/div[2]/a[2]/span[1]')
    first_product = (By.XPATH, "(//li[contains(@class, 'product-base')])[1]")

    def hover_on_men_menu(self, action_chains):
        men_element = self.driver.find_element(*self.men_link)
        action_chains.move_to_element(men_element).perform()
        return self

    def click_casual_tshirts(self):
        self.driver.find_element(*self.casual_tshirt_link).click()
        time.sleep(2)
        return self

    def click_first_product(self):
        # Wait for products to load
        wait = WebDriverWait(self.driver, 10)
        first_product = wait.until(EC.element_to_be_clickable(self.first_product))
        first_product.click()
        time.sleep(3)
        return self

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
        time.sleep(3)
        return self