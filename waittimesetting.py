from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://xdclass.net")
# driver.implicitly_wait(10)
try:
    ele = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".login > span:nth-child(2)")))
    ele.click()
    print("加载成功")
    print(driver.title)
except:
    print("加载失败")