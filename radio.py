from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("file:///D:/BaiduNetdiskDownload/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E5%85%B6%E4%BB%96%E8%B5%84%E6%96%99/%E7%AC%AC6%E7%AB%A0/%E7%AC%AC1%E9%9B%86/ratio.html")
driver.find_element_by_css_selector("#female").click()
