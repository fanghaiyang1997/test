import unittest
import HTMLTestRunner
import time


class UnitTestCase(unittest.TestCase):
    def SetUp(self):
        print("setup")

    def TearDown(self):
        print("TearDown")

    def test_one(self):
        print("test_one")

    def test_two(self):
        print("test_two")

    def test_three(self):
        print("test_three")

    def test_four(self):
        print("test_four")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UnitTestCase("test_two"))
    suite.addTest(UnitTestCase("test_one"))
    suite.addTest(UnitTestCase("test_three"))
    suite.addTest(UnitTestCase("test_four"))
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    fp = open('./' + file_prefix + '_result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况:')
    runner.run(suite)
    fp.close()
