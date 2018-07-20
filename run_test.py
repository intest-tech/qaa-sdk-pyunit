import unittest


class DemoTestCase(unittest.TestCase):
    def test_pass(self):
        """
        test_pass
        :return: 
        """
        a = 1
        self.assertEqual(1, a, msg='not match')

    def test_fail(self):
        """
         stest_fail sad sf
         asdf safd
         :return:
        """
        a = 1
        self.assertEqual(2, a, msg='not match')

    def test_error(self):
        """
        test_error s
        :return: 
        """
        a = {'a': 1}
        a.print
        self.assertEqual(1, a, msg='not match')

    @unittest.skip('test skip')
    def test_skip(self):
        """
        test_skip
        :return: 
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
    upload_result = qaa_reporter.post(result, version='18.0.0.1')
    print(upload_result)
