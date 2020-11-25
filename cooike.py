from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("https://xdclass.net")
print(driver.title)
driver.implicitly_wait(10)
driver.add_cookie({"name": "name", "value": "EbbTide"})
driver.add_cookie({"name": "token", "value": "xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMTcuanBlZyIsImlkIjo2NzgxNTAyLCJuYW1lIjoiRWJiVGlkZSIsImlhdCI6MTYwNTc1NjQ2NCwiZXhwIjoxNjA2MzYxMjY0fQ.BSZMmgUd0E6bdR7PufToxH4RabNIa9oymH6qecrbSEA"})
try:
    ele1 = driver.find_element_by_css_selector("div.othercourse:nth-child(3) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)")
    ele1.click()
except:
    driver.get_screenshot_as_file("./error_png.png")