import unittest
from selenium import webdriver
from time import sleep


class RetTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("start")
        self.driver = webdriver.Chrome()
        self.driver.get("file:///D:/study/study/day01.html")

    def TearDown(self):
        print("end")
        pass

    def test_reset1(self):
        driver = self.driver
        driver.find_element_by_css_selector("body > div > form > input[type=text]:nth-child(1)").send_keys("初夏")
        sleep(2)
        driver.find_element_by_css_selector("body > div > form > input[type=password]:nth-child(4)").send_keys("654321")
        sleep(2)

        driver.find_element_by_css_selector("body > div > form > input[type=text]:nth-child(7)").send_keys("csdn")
        sleep(2)

        driver.find_element_by_css_selector("body > div > form > input[type=text]:nth-child(11)").send_keys("152322645")
        sleep(2)

        driver.find_element_by_css_selector("body > div > form > input[type=radio]:nth-child(16)").click()
        sleep(2)

        driver.find_element_by_css_selector("body > div > form > input[type=checkbox]:nth-child(21)").click()
        sleep(2)

        driver.find_element_by_css_selector("body > div > form > input[type=checkbox]:nth-child(22)").click()
        sleep(2)

        driver.find_element_by_css_selector("body > div > form > textarea").send_keys("one day,one dream")
        sleep(2)

        driver.find_element_by_css_selector("body > div > form > input[type=reset]:nth-child(28)").click()


if __name__ == '__main__':
    unittest.main()
