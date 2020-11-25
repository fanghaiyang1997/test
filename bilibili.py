import unittest
import time

from selenium import webdriver


class UserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("测试开始")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def tearDown(self) -> None:
        print("测试结束")
        pass

    def test_search(self):
        u"搜索B站"
        driver = self.driver
        ele1 = driver.find_element_by_id("kw")
        ele1.send_keys("哔哩哔哩")
        ele2 = driver.find_element_by_id("su")
        ele2.click()


if __name__ == '__main__':
    unittest.main()
