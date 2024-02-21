import requests
import time


class CreateNote:
    host = 'http://note-api.wps.cn'

    def create_note(self, userid, sid, num):
        notes_list = []
        for i in range(num):
            # 前置
            headers = {
                'Content-Type': 'application/json',
                'Cookie': f'wps_sid={sid}',
                'X-user-key': str(userid)
            }
            note_id = str(int(time.time() * 1000)) + '_noteId'
            body = {
                'noteId': note_id
            }
            res = requests.post(url=self.host + '/v3/notesvr/set/noteinfo', headers=headers, json=body)
            infoVersion = res.json()['infoVersion']
            body = {
                'noteId': note_id,
                'title': 'test',
                'summary': 'test',
                'body': 'test',
                'localContentVersion': infoVersion,
                'BodyType': 0

            }
            notes_list.append(body)
            requests.post(url=self.host + '/v3/notesvr/set/notecontent', headers=headers, json=body)
        return notes_list
