from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
sleep(2)
driver.get("https://xdclass.net")

step1 = driver.find_element_by_css_selector(".login > span:nth-child(2)")
ActionChains(driver).click(step1).perform()
sleep(2)
step2 = driver.find_element_by_css_selector(".mobienum > input:nth-child(1)")
step2.send_keys("18321703275")
sleep(2)
step3 = driver.find_element_by_css_selector(".psw > input:nth-child(1)")
step3.send_keys("fhylovecz1997mma")
sleep(2)
step4 = driver.find_element_by_css_selector(".btn")
step4.click()
sleep(2)
step5 = driver.find_element_by_css_selector(".avatar_img")
sleep(2)
print("==测试结果==")
name = step5
if name == "EbbTide":
    print("login success")
else:
    print("login fail")


driver.quit()
