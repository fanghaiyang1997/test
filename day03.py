import unittest
import time


class UnitForTest(unittest.case):

    def SetUp(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test_01(self):
        print("test1")

    def test_02(self):
        print("test2")


if __name__ == '__main__':
    unittest.main()
