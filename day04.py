from time import sleep

from selenium import webdriver

chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

driver = webdriver.Chrome(executable_path = chrome_driver)
driver.get("https://bbclsop-test.mshuoke.com/login")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/form/div[1]/div/div/div[2]/input").send_keys("fanghaiyang")
sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/form/div[2]/div/div/div[2]/input").send_keys("123456")
sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/form/div[3]/div/button").click()
sleep(2)

driver.quit()
