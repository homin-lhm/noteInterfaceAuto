import unittest
import requests
from common.checkMethods import CheckMethod
from businessCommon.clearNote import Clear
from businessCommon.create import CreateNote
from copy import deepcopy
import time


class TestPro(unittest.TestCase):
    host = 'http://note-api.wps.cn'
    userid = '922061821'
    sid = 'V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd'
    expect = {"responseTime": int, "webNotes": [
        {"noteId": "d54930427dd4ebd9679002c584b0787f", "createTime": int, "star": 0, "remindTime": 0,
         "remindType": 0, "infoVersion": 1, "infoUpdateTime": int, "groupId": None,
         "title": "75u8dlZyTLqWCm/b2PLNlg==", "summary": "pIDnRrCwq8sUW3gyWpo7iw==", "thumbnail": None,
         "contentVersion": 3, "contentUpdateTime": int}]}

    def setUp(self) -> None:
        Clear().clear_note(self.userid, self.sid)

    def testCase01_major(self):
        """获取首页主流程"""
        # 前置
        c_res = CreateNote().create_note(self.userid, self.sid, 1)
        # 操作
        startindex = 0
        rows = 10
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        headers = {
            'Cookie': f'wps_sid={self.sid}'
        }
        res = requests.get(url=self.host + path, headers=headers)
        print(res.status_code)
        print(res.text)
        expect = deepcopy(self.expect)
        expect['webNotes'][0]['noteId'] = c_res[0]['noteId']
        expect['webNotes'][0]['title'] = c_res[0]['title']
        expect['webNotes'][0]['summary'] = c_res[0]['summary']
        expect['webNotes'][0]['contentVersion'] = c_res[0]['localContentVersion']
        CheckMethod().output_check(expect, res.json())
