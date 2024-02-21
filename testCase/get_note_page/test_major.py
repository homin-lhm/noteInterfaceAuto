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


@class_case_log
class GetPageNotesMajor(unittest.TestCase):
    envConfig = YamlRead().env_config()
    host = envConfig['host']
    userid1 = envConfig['userId1']
    sid1 = envConfig['sid1']

    expect = {"responseTime": int, "webNotes": [
        {"noteId": "d54930427dd4ebd9679002c584b0787f", "createTime": int, "star": 0, "remindTime": 0,
         "remindType": 0, "infoVersion": 1, "infoUpdateTime": int, "groupId": None,
         "title": "75u8dlZyTLqWCm/b2PLNlg==", "summary": "pIDnRrCwq8sUW3gyWpo7iw==", "thumbnail": None,
         "contentVersion": 3, "contentUpdateTime": int}]}

    def setUp(self) -> None:
        Clear().clear_note(self.userid1, self.sid1)

    def testCase01_major(self):
        """获取首页主流程"""
        step('用户A新增一条便签数据')
        c_res = CreateNote().create_note(self.userid1, self.sid1, 1)
        step('用户A请求获取首页便签接口')
        startindex = 0
        rows = 10
        path = f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = ApiRe().get(url=self.host + path, sid=self.sid1)
        self.assertEqual(200, res.status_code)
        expect = deepcopy(self.expect)
        expect['webNotes'][0]['noteId'] = c_res[0]['noteId']
        expect['webNotes'][0]['title'] = c_res[0]['title']
        expect['webNotes'][0]['summary'] = c_res[0]['summary']
        expect['webNotes'][0]['contentVersion'] = c_res[0]['localContentVersion']
        CheckMethod().output_check(expect, res.json())
