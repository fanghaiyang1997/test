import unittest
import HTMLTestRunner
import time


class day05TestCase(unittest.TestCase):
    def SetUp(self):
        print("SetUp")

    def TearDown(self):
        print("TearDown")

    def test_01(self):
        u"第一条测试用例"
        print("test_01")

    def test_02(self):
        u"第二条测试用例"
        print("test_02")

    def test_03(self):
        u"第三条测试用例"
        print("test_03")

    def test_04(self):
        u"第四条测试用例"
        print("test_04")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(day05TestCase("test_01"))
    suite.addTest(day05TestCase("test_02"))
    suite.addTest(day05TestCase("test_03"))
    suite.addTest(day05TestCase("test_04"))
    day05 = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    fp = open('./' + day05 + '_result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'测试执行情况')
    runner.run(suite)
    fp.close()
