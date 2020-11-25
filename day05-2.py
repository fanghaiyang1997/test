import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import HTMLTestRunner


class UnitTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("file:///D:/study/study/day01.html")

    def TearDown(self):
        print("end")
        pass

    def test_01(self):
        driver = self.driver
        step1 = driver.find_element_by_css_selector("body > div > form > input[type=text]:nth-child(1)")
        step1.send_keys("fanghiayang")
        sleep(2)

    def test_02(self):
        driver = self.driver
        step2 = driver.find_element_by_css_selector("body > div > form > input[type=password]:nth-child(4)")
        step2.send_keys("fhylovecz1997mma")
        sleep(2)

    def test_03(self):
        driver = self.driver
        step3 = driver.find_element_by_css_selector("body > div > form > input[type=text]:nth-child(7)")
        step3.send_keys("okls")
        sleep(2)

    def test_04(self):
        driver = self.driver
        step3 = driver.find_element_by_css_selector("body > div > form > input[type=text]:nth-child(11)")
        step3.send_keys("3050329462")
        sleep(2)
        step4 = driver.find_element_by_css_selector("body > div > form > select")
        ActionChains(driver).click(step4).perform()
        sleep(2)

    def test_05(self):
        driver = self.driver
        step5 = driver.find_element_by_css_selector("body > div > form > input[type=radio]:nth-child(16)")
        ActionChains(driver).click(step5).perform()
        sleep(2)

    def test_06(self):
        driver = self.driver
        step6 = driver.find_element_by_css_selector("body > div > form > textarea")
        step6.send_keys("一个好人")
        sleep(2)

    def test_07(self):
        driver = self.driver
        step7 = driver.find_element_by_css_selector("body > div > form > input[type=reset]:nth-child(28)")
        ActionChains(driver).click(step7).perform()
        sleep(2)

    def test_08(self):
        driver = self.driver
        step8 = driver.find_element_by_partial_link_text("百度一下")
        ActionChains(driver).click(step8).perform()
        sleep(2)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UnitTestCase("test_01"))
    suite.addTest(UnitTestCase("test_02"))
    suite.addTest(UnitTestCase("test_03"))
    suite.addTest(UnitTestCase("test_04"))
    suite.addTest(UnitTestCase("test_05"))
    suite.addTest(UnitTestCase("test_06"))
    suite.addTest(UnitTestCase("test_07"))
    suite.addTest(UnitTestCase("test_08"))
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    fp = open('./' + file_prefix + '_result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况:')
    runner.run(suite)
    fp.close()

