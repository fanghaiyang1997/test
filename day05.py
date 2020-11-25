from selenium import webdriver
import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://xdclass.net")
driver.implicitly_wait(10)

step1 = driver.find_element_by_css_selector(".login > span:nth-child(2)")
ActionChains(driver).click(step1).perform()
driver.implicitly_wait(10)

step2 = driver.find_element_by_css_selector(".mobienum > input:nth-child(1)")
step2.send_keys("18321703275")
driver.implicitly_wait(10)

step3 = driver.find_element_by_css_selector(".psw > input:nth-child(1)")
step3.send_keys("fhylovecz1997mma")
driver.implicitly_wait(10)

step4 = driver.find_element_by_css_selector(".btn")
step4.click()
driver.implicitly_wait(10)

ele1 = driver.find_element_by_css_selector(".list_item > li:nth-child(3)")
ActionChains(driver).move_to_element(ele1).perform()
driver.implicitly_wait(10)

ele2 = driver.find_element_by_css_selector(".deep > div:nth-child(3) > a:nth-child(1)")
ActionChains(driver).click(ele2).perform()
driver.implicitly_wait(10)

ele3 = driver.find_element_by_css_selector(".courselist > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)")
ActionChains(driver).click(ele3).perform()
driver.implicitly_wait(10)

ele4 = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div[1]/div[1]/span")
ActionChains(driver).click(ele4).perform()
driver.implicitly_wait(10)
