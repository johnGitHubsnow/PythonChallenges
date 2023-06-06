import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

#Launch Chrome browser
driver = webdriver.Chrome(executable_path= r"C:\Users\7000033861\Downloads\chromedriver_win32\chromedriver.exe")

# Step 1: Open amazon.com
driver.get("https://www.amazon.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# Step 2: Search for "sony wh-1000xm5"
driver.find_element(By.XPATH, "//input[@placeholder = 'Search Amazon']").send_keys("sony wh-1000xm5")
driver.implicitly_wait(10)
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.implicitly_wait(10)

# Step 3: Select 1st product
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sony WH-1000XM5').click()
driver.implicitly_wait(10)

# Step 4: Click on sign-in using ActionChains class
locator = driver.find_element(By.XPATH, "//span[text() = 'Hello, sign in']")
action = ActionChains(driver)
mouse_act = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator))
action.move_to_element(mouse_act).perform()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//span[text() = 'Sign in']").click()
driver.implicitly_wait(10)

# Step 5: Pass phone number
driver.find_element(By.XPATH, "//input[@type = 'email' and @id = 'ap_email']").send_keys("8328367838674")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@type = 'submit' and @id = 'continue']").click()

# Step 6: Handle phone number validation
if "Incorrect phone number" in driver.page_source:
    driver.save_screenshot("Error_Screenshot2.png")
else:
    driver.implicitly_wait(10)
    # Phone number is valid, re-launch amazon.com
    driver.get("https://www.amazon.com/")
    print("------------------------------------Test case is Passed -------------------------------")

driver.quit()




