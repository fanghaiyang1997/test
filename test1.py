import unittest
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class LoginOrderTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url = "file:///D:/study/study/day01.html"
        self.driver.get(self.base_url)

    def tearDown(self):
        print("单个测试用例结束")
        pass
        # 单个测试用例结束

    def test_login_order(self):
        u"测试用例"
        driver = self.driver
        username = driver.find_element_by_css_selector("body > div > form > input[type=text]:nth-child(1)")
        username.send_keys("陈拾")

        step2 = driver.find_element_by_css_selector("body > div > form > input[type=password]:nth-child(4)")
        step2.send_keys("fhylovecz1997mma")
        sleep(2)

        step3 = driver.find_element_by_css_selector("body > div > form > input[type=text]:nth-child(7)")
        step3.send_keys("okls")
        sleep(2)

        step3 = driver.find_element_by_css_selector("body > div > form > input[type=text]:nth-child(11)")
        step3.send_keys("3050329462")
        sleep(2)
        step4 = driver.find_element_by_css_selector("body > div > form > select")
        ActionChains(driver).click(step4).perform()
        sleep(2)

        step5 = driver.find_element_by_css_selector("body > div > form > input[type=radio]:nth-child(16)")
        ActionChains(driver).click(step5).perform()
        sleep(2)

        step6 = driver.find_element_by_css_selector("body > div > form > textarea")
        step6.send_keys("一个好人")
        sleep(2)

        step6 = driver.find_element_by_css_selector("body > div > form > input[type=reset]:nth-child(28)")
        ActionChains(driver).click(step6).perform()
        sleep(2)

        step8 = driver.find_element_by_partial_link_text("百度一下")
        ActionChains(driver).click(step8).perform()
        sleep(2)
        print("测试结果")


if __name__ == '__main__':
    unittest.main()