'''
1.通过unittest框架将单个的test case结合 自动调用测试用例
2.并通过unittest和HTMLTestRunner框架结合，输出html格式的测试报告
3.一直无法输出html文件，可查询链接：https://www.cnblogs.com/hanmk/p/8656574.html
'''

#-*-coding：UTF:8-*-
import unittest
import HTMLTestRunner
import os
from TestCase.Login import get_token


class TestCase_Get_Token(unittest.TestCase):
    '调用unittest框架，将接口请求和测试case结合'
    def test_001(self):
        url = get_token.PATH + '/api/uaa/oauth/token'
        head = {
            'content-type': 'application/x-www-form-urlencoded'
        }
        data = {
            'client_id': 'ua',
            'grant_type': 'onetime',
            'mobile': '17316326189',
            'token': '123456'
        }
        result = get_token.Login_Get_User_Token(url, head, data)
        #print(json.dumps(result, indent=2,ensure_ascii=True))
        '利用unittest断言来判断case是否执行成功与失败' \
        '常用self.assertEqual()  判断是否相等' \
        'self.assertNotEqual() 判断是否不等' \
        'self.assertTrue() 判断返回是否为真或假'
        self.assertEqual(result.status_code,200,'测试失败')



if __name__=='__main__':
    filepath = '../Reports/test.html'
    fp = open(filepath, 'w+')
    suite = unittest.TestSuite()
    suite.addTest(TestCase_Get_Token('test_001'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,output=filepath,report_title='test-report-001',descriptions='测试结果如下：')
    runner.run(suite)
    fp.close()


