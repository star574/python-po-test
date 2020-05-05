import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 初始自动化环境
        pass

    def testCase1(self):  #
        pass

    def testCase2(self):  #
       pass

    @classmethod
    def tearDownClass(cls):  # 清除环境
        pass

if __name__ == "__main__":
    s = unittest.main()