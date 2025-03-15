import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver):
        self.driver = driver


    def handle_notification(self):
        """Handles notification popup if it appears."""
        try:
            # Wait for the notification pop-up (if it appears)
            wait = WebDriverWait(self.driver, 5)  # Wait up to 5 seconds
            block_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Block']")))

            # Click the "Block" button
            block_button.click()
            print("Notification blocked.")
        except:
            # If pop-up does not appear, continue with execution
            print("No notification pop-up appeared.")

    def switch_to_product_window(self):
        """Switches to the product window if it opens in a new tab."""
        window_ids = self.driver.window_handles
        for window_id in window_ids:
            self.driver.switch_to.window(window_id)
            print(f"Switched to window with title: {self.driver.title}")

    def select_size(self):
        """Selects a size on the product page using exact XPath."""
        # Wait for a moment to ensure page is loaded
        time.sleep(3)

        # Handle notification popup
        self.handle_notification()

        # Switch to the correct window
        self.switch_to_product_window()

        # Click on the size button using the exact XPath from the shared code
        size_button = self.driver.find_element(By.XPATH, '//*[@id="sizeButtonsContainer"]/div[2]/div[2]/div[1]/button')
        size_button.click()
        time.sleep(2)

        # Get the size text for validation
        size = size_button.text
        print(f"Selected size: {size}")
        return size

    def add_to_bag(self):
        """Clicks on the 'Add to Bag' button using exact XPath."""
        # Click on the Add to Bag button using the exact XPath from the shared code
        add_to_bag_button = self.driver.find_element(By.XPATH,
                                                     '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]')
        add_to_bag_button.click()
        time.sleep(3)
        print("Added to bag successfully.")

    def get_product_details(self):
        """Fetches product details like title and price using exact XPaths."""
        # Get product title using the exact XPath from the shared code
        title = self.driver.find_element(By.XPATH,
                                         '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/h1[1]').text

        # Get product price using the exact XPath from the shared code
        price = self.driver.find_element(By.XPATH,
                                         '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/p[1]/span[1]/strong').text
        size = self.driver.find_element(By.XPATH,'//*[@id="sizeButtonsContainer"]/div[2]/div[2]/div[1]/button').text

        product_details = {
            "title": title,
            "price": price,
            "size":size
        }

        print(f"Product Name: {title}")
        print(f"Product Price: {price}")
        print(f"Product size: {size}")
        return product_details

    def navigate_to_cart(self):
        """Navigates to the cart page using exact XPath."""
        cart_button = self.driver.find_element(By.XPATH, '//*[@id="desktop-header-cnt"]/div[2]/div[2]/a[2]/span[1]')
        cart_button.click()
        time.sleep(3)
        print("Navigated to cart page.")