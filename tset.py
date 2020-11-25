# 导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# 指定浏览器
driver = webdriver.Firefox()
sleep(2)
# 要进行测试得ip
driver.get("https://xdclass.net")

# 各种定位方法
# driver.find_element_by_class_name().send_keys()
# sleep(2)
# driver.find_element_by_name().send_keys()
# sleep(2)
# driver.find_element_by_id().send_keys()
# sleep(2)
# driver.find_element_by_link_text().click()
# sleep(2)
# driver.find_element_by_partial_link_text().click()
# sleep(2)
# driver.find_element_by_tag_name().send_keys()
# sleep(2)
ele1 = driver.find_element_by_css_selector(".list_item > li:nth-child(3)")
ActionChains(driver).move_to_element(ele1).perform()
sleep(2)
ele2 = driver.find_element_by_css_selector(".base > div:nth-child(3) > a:nth-child(12)")
ele2.click()
sleep(2)
# driver.find_element_by_xpath().send_keys()
# sleep(2)
# 退出
driver.quit()
