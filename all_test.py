import unittest
import HTMLTestRunner
import time
import submit,reset


def sum_suite():
    print("start")
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(submit.SubTestCase))
    suite.addTest(unittest.makeSuite(reset.RetTestCase))
    return suite


if __name__ == '__main__':
    case = sum_suite()

    first = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
    second = open("./" + first + "result.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=second, title="学生爱好调查", description=u"测试执行情况", verbosity=2 )
    runner.run(case)
    second.close()
print("end")
