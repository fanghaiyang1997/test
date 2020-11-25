import unittest
import time
import HTMLTestRunner
import day06,bilibili


def create_suite():
    print("测试开始")
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(day06.UserTestCase))
    suite.addTest(unittest.makeSuite(bilibili.UserTestCase))
    return suite


if __name__ == '__main__':
    suite = create_suite()

    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    fp = open("./" + file_prefix + "_result.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"B站搜索 测试报告", description=u"测试用例执行情况", verbosity=2)
    runner.run(suite)
    fp.close()
print("测试结束")