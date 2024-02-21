import unittest
from BeautifulReport import BeautifulReport
import os

ENVIRON = "Online"  # 线上 Online 测试环境 Offline
Dir = os.path.dirname(os.path.abspath(__file__))


def run(test_suite):
    # 定义输出的文件位置和名字
    filename = "report.html"
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description='测试报告', report_dir='./')


if __name__ == '__main__':
    run_pattern = 'test_input'  # all 全量测试用例执行/smoking 冒烟测试执行/指定执行文件
    if run_pattern == 'all':
        pattern = 'test_*.py'
    elif run_pattern == 'smoking':
        pattern = 'test_major*.py'
    else:
        run_pattern = run_pattern + '.py'
    suite = unittest.TestLoader().discover('./testCase', pattern=run_pattern)

    run(suite)
