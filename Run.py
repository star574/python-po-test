import Clean
import unittest
import HTMLTestRunner
# from Common.Report import HTML_FILE_PATH, HTML_FILE_NAME

# 一键清理日志,测试数据,测试报告,测试截图
Clean.Clean()
# from Common.RunTime_Log import Log

Case_Dir = r'E:\ZenTao_Test_Project\TestCases'
# file = open(HTML_FILE_PATH + HTML_FILE_NAME, 'wb')
suite = unittest.defaultTestLoader.discover(Case_Dir, pattern='Test_Case_ZenTao_Login.py')
# runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='禅道登录测试报告', description='用例执行情况')
# runner.run(suite)
# Log().W_log_warning("写入测试报告")
print('测试结束')
# file.close()
