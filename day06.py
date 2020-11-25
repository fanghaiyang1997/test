from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest


class UserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("Start")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.baidu.com")

    def TearDown(self):
        print("End")
        pass

    def test_01(self):
        driver = self.driver
        ele1 = driver.find_element_by_id("kw")
        ele1.send_keys("bilibili")
        sleep(2)

        ele2 = driver.find_element_by_id("su")
        ActionChains(driver).click(ele2).perform()
        sleep(2)


if __name__ == '__main__':
    unittest.main()


