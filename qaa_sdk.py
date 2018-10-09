import json
import time
import requests
import unittest

API_ADDR = 'http://localhost:5000'
WEB_DOMAIN = 'http://localhost'
API_TOKEN = '48f6011f8803498db4468a4f32ed7140'


def set_result(test_results: unittest.TestResult, **kwargs):
    """
    提取unittest中的测试结果
    :param test_results: unittest.TestResult
    :return:
    """
    total = test_results.testsRun
    failures = len(test_results.failures)
    errors = len(test_results.errors)
    skipped = len(test_results.skipped)
    success = total - failures - errors - skipped

    # overview
    res_dict = dict(
        was_successful=test_results.wasSuccessful(),
        total=total,
        failures=failures,
        errors=errors,
        success=success,
        skipped=skipped
    )
    res_dict.update(kwargs)

    # traceback
    failure_list = []  # 失败的内容
    for x in test_results.failures:
        case_name = x[0]._testMethodName
        method_doc = x[0]._testMethodDoc  # 给测试脚本写的文档
        assert method_doc is not None, ('请给测试用例%s函数写上文档注释' % case_name)
        note_data = {
            'case_name': case_name,
            'explain': method_doc.replace('\n', '').strip().replace('        ', ', '),
            'status': 'failures',
            'note': x[1]
        }
        failure_list.append(note_data)

    for x in test_results.errors:
        case_name = x[0]._testMethodName
        method_doc = x[0]._testMethodDoc  # 给测试脚本写的文档
        assert method_doc is not None, ('请给测试用例%s函数写上文档注释' % case_name)
        note_data = {
            'case_name': case_name,
            'explain': method_doc.replace('\n', '').strip().replace('        ', ', '),
            'status': 'errors',
            'note': x[1]
        }
        failure_list.append(note_data)

    res_dict['details'] = failure_list

    return res_dict


class TestReport(object):
    """
    测试报告自动化上传接口封装之后的类
    """

    def __init__(self):
        self.base_url = API_ADDR
        self.token = API_TOKEN
        self.start_time = time.time()

    def post(self, test_results: unittest.TestResult, **kwargs):
        """
        将接口测试结果给发送到服务器
        :param test_results: unittest.TestResult
        :return:
        """
        duration = time.time() - self.start_time
        url = '%s/api/test-result/upload?token=%s' % (self.base_url, self.token)
        res = requests.post(url, json=set_result(test_results, duration=round(duration, 3), **kwargs))
        res_dict = json.loads(res.text)
        return res_dict


qaa_reporter = TestReport()
