from selenium import webdriver
import pandas as pd
from openpyxl.workbook import Workbook
from selenium.webdriver.common.by import By

#Launch Chrome browser
driver = webdriver.Chrome(executable_path= r"C:\Users\7000033861\Downloads\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()

# Step 1: Open news.google.com
driver.get("https://news.google.com")
driver.implicitly_wait(10)



# Step 2: Go to the Technology news page
driver.find_element(By.XPATH, "//a[@class = 'brSCsc' and @jsname = 'sCfAK' and @aria-label = 'Technology']").click()
driver.implicitly_wait(10)

# Step 3: Scrape the first 10 highlighted news
news_list = []
for i in range(1,11):
    title = driver.find_element(By.XPATH ,f"(//h4[@class = 'gPFEn'])[{i}]").text
    print(title)
    url = driver.find_element(By.XPATH, f"(//div[@class = 'XlKvRb' and @jsaction = 'click:KjsqPd;'])[{i}]/a").get_attribute("href")
    print(url)
    date = driver.find_element(By.XPATH, f"(//div[@class = 'UOVeFe Jjkwtf']/child :: time )[{i}]").get_attribute("textContent")
    print(date)

    news_list.append({"Title": title, "URL": url, "Date": date})

# Step 4: Create an Excel sheet with news title, URL, and date
df = pd.DataFrame(news_list)
df.to_excel("top_news3.xlsx")

driver.quit()
