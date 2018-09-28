import unittest


class DemoTestCase(unittest.TestCase):
    def test_pass(self):
        """
        test_pass
        """
        a = 1
        self.assertEqual(1, a, msg='not match')

    def test_fail(self):
        """
         stest_fail sad sf
         asdf safd
        """
        a = 1
        self.assertEqual(2, a, msg='not match')

    def test_error(self):
        """
        test_error s
        """
        a = {'a': 1}
        a.print
        self.assertEqual(1, a, msg='not match')

    @unittest.skip('test skip')
    def test_skip(self):
        """
        test_skip
        """
        a = 1
        self.assertEqual(1, a, msg='not match')


if __name__ == '__main__':
    from qaa_sdk import qaa_reporter

    suite = unittest.TestSuite()
    suite.addTest(DemoTestCase('test_pass'))
    suite.addTest(DemoTestCase('test_fail'))
    suite.addTest(DemoTestCase('test_error'))
    suite.addTest(DemoTestCase('test_skip'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    upload_result = qaa_reporter.post(result, version='18.9.26.1', stage='接口测试', tag='local')
    print(upload_result)
