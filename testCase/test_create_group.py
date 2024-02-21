import unittest
import requests
from parameterized import parameterized


class TestPro(unittest.TestCase):

    def setUp(self) -> None:
        print('SETUP')
        print('init login 5line@@@@@@@@@')

    @parameterized.expand(['groupId', 'groupName', 'order'])
    def testCase01_major(self, key):
        """新增分组主流程"""
        print('----------------------------------------')
        print('testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notegroup'
        headers = {
            'Cookie': 'wps_sid=V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd',
            'X-User-Key': '922061821',
            'Content-Type': 'application/json'
        }
        groupId = '111111'
        data = {
            'groupId': groupId,
            'groupName': '旅游笔记',
            'order': 0
        }
        data.pop(key)
        res = requests.post(url=host + path, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg='状态码异常，期望的状态XXX')
        self.assertIn('responseTime', res.json().keys())
        self.assertIn('updateTime', res.json().keys())
        self.assertEqual(2, len(res.json().keys()))
        self.assertEqual(int, type(res.json()['responseTime']))

        assert_res = requests.post(url=host + '/v3/notesvr/get/notegroup', headers=headers,
                                   json={'excludeInvalid': True})
        a = False
        for i in assert_res.json()['noteGroups']:
            if i['groupId'] == groupId:
                a = True

        self.assertEqual(True, a)

    def testCase02_input(self):
        """新增分组groupId字段缺失"""
        print('----------------------------------------')
        print('testCase02_input')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notegroup'
        headers = {
            'Cookie': 'wps_sid=V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd',
            'X-User-Key': '922061821',
            'Content-Type': 'application/json'
        }
        groupId = '111111'
        data = {
            'groupId': groupId,
            'groupName': '旅游笔记',
            'order': 0
        }
        data.pop('groupId')
        res = requests.post(url=host + path, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        assert res.status_code == 500

