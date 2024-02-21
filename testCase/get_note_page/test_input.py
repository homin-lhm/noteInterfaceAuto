import unittest
import requests
from common.checkMethods import CheckMethod
from businessCommon.clearNote import Clear
from businessCommon.create import CreateNote
from copy import deepcopy
from common.logCreate import info, step, error, class_case_log
from common.yamlRead import YamlRead
import time
from businessCommon.apiRe import ApiRe
from parameterized import parameterized


@class_case_log
class GetPageNotesInput(unittest.TestCase):
    envConfig = YamlRead().env_config()
    host = envConfig['host']
    userid1 = envConfig['userId1']
    sid1 = envConfig['sid1']
    startindexError = [[{'value': -1, 'code': 200}], [{'value': '啊ab', 'code': 500}], [{'value': None, 'code': 500}]]

    expect = {"responseTime": int, "webNotes": [
        {"noteId": "d54930427dd4ebd9679002c584b0787f", "createTime": int, "star": 0, "remindTime": 0,
         "remindType": 0, "infoVersion": 1, "infoUpdateTime": int, "groupId": None,
         "title": "75u8dlZyTLqWCm/b2PLNlg==", "summary": "pIDnRrCwq8sUW3gyWpo7iw==", "thumbnail": None,
         "contentVersion": 3, "contentUpdateTime": int}]}

    def setUp(self) -> None:
        Clear().clear_note(self.userid1, self.sid1)

    # def testCase01_input(self):
    #     """过期的wps_id"""
    #     step('用户A新增一条便签数据')
    #     c_res = CreateNote().create_note(self.userid1, self.sid1, 1)
    #     step('用户A请求获取首页便签接口')
    #     startindex = 0
    #     rows = 10
    #     path = f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
    #     res = ApiRe().get(url=self.host + path, sid='V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd')
    #     self.assertEqual(401, res.status_code)
    #     expect = {
    #         'errorCode': -2010,
    #         'errorMsg': str
    #     }
    #     CheckMethod().output_check(expect, res.json())
    #
    # def testCase02_input(self):
    #     """非法的wps_id"""
    #     step('用户A新增一条便签数据')
    #     c_res = CreateNote().create_note(self.userid1, self.sid1, 1)
    #     step('用户A请求获取首页便签接口')
    #     startindex = 0
    #     rows = 10
    #     path = f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
    #     res = ApiRe().get(url=self.host + path, sid='@@32132123简')
    #     self.assertEqual(401, res.status_code)
    #     expect = {
    #         'errorCode': -2010,
    #         'errorMsg': str
    #     }
    #     CheckMethod().output_check(expect, res.json())
    #
    # def testCase03_input(self):
    #     """wps_id缺失"""
    #     step('用户A新增一条便签数据')
    #     c_res = CreateNote().create_note(self.userid1, self.sid1, 1)
    #     step('用户A请求获取首页便签接口')
    #     startindex = 0
    #     rows = 10
    #     path = f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
    #     res = ApiRe().get(url=self.host + path, headers={})
    #     self.assertEqual(401, res.status_code)
    #     expect = {
    #         'errorCode': -2010,
    #         'errorMsg': str
    #     }
    #     CheckMethod().output_check(expect, res.json())

    @parameterized.expand(startindexError)
    def testCase04_input(self, dic):
        """startindex 异常值校验"""
        step('用户A新增一条便签数据')
        c_res = CreateNote().create_note(self.userid1, self.sid1, 1)
        step('用户A请求获取首页便签接口')
        startindex = dic['value']
        rows = 10
        path = f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = ApiRe().get(url=self.host + path, sid=self.sid1)
        self.assertEqual(dic['code'], res.status_code)
        expect = {
            'errorCode': -7,
            'errorMsg': "参数类型错误！"
        }
        CheckMethod().output_check(expect, res.json())

