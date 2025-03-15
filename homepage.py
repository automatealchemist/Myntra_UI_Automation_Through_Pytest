import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
driver.maximize_window()
driver.get("https://www.myntra.com")
time.sleep(5)
try:
    # Wait for the notification pop-up (if it appears)
    wait = WebDriverWait(driver, 5)  # Wait up to 5 seconds
    block_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Block']")))

    # Click the "Block" button
    block_button.click()
    print("Notification blocked.")
except:
    # If pop-up does not appear, continue with execution
    print("No notification pop-up appeared.")
act= ActionChains(driver)
#men = driver.find_element(By.LINK_TEXT,'MEN')
act.move_to_element(driver.find_element(By.LINK_TEXT,'MEN')).perform()



time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="desktop-header-cnt"]/div[2]/nav/div/div[1]/div/div/div/div/li[1]/ul/li[2]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="31598736"]/a/div[1]/div/div/div/picture/img').click()
#time.sleep(0)
#driver.switch_to.alert.dismiss()

# item detail page
time.sleep(3)
try:
    # Wait for the notification pop-up (if it appears)
    wait = WebDriverWait(driver, 5)  # Wait up to 5 seconds
    block_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Block']")))

    # Click the "Block" button
    block_button.click()
    print("Notification blocked.")
except:
    # If pop-up does not appear, continue with execution
    print("No notification pop-up appeared.")
windowIDs = driver.window_handles
for windowID in windowIDs:
    driver.switch_to.window(windowID)
    print(driver.title)

driver.find_element(By.XPATH,'//*[@id="sizeButtonsContainer"]/div[2]/div[2]/div[1]/button').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]').click()
time.sleep(3)
size = driver.find_element(By.XPATH,'//*[@id="sizeButtonsContainer"]/div[2]/div[2]/div[1]/button').text
print(size)

t_shirt_title = driver.find_element(By.XPATH,'//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/h1[1]').text
print(t_shirt_title)
t_shirt_price = driver.find_element(By.XPATH,'//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/p[1]/span[1]/strong').text
print(t_shirt_price)
driver.find_element(By.XPATH,'//*[@id="desktop-header-cnt"]/div[2]/div[2]/a[2]/span[1]').click()
time.sleep(3)


#cart page
cart_t_shirt_title= driver.find_element(By.XPATH,'//*[@id="cartItemsList"]/div/div/div/div[2]/div[2]/div/div[1]/div').text
print(cart_t_shirt_title)
cart_t_shirt_price = driver.find_element(By.XPATH,'//*[@id="cartItemsList"]/div/div/div/div[2]/div[2]/div/div[4]/div[1]/div').text
print(cart_t_shirt_price)
cart_t_shirt_size = driver.find_element(By.XPATH,'//*[@id="cartItemsList"]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/span').text
print(cart_t_shirt_size)

driver.quit()


