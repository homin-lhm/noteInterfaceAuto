import requests
from common.logCreate import info, error
import json


class ApiRe:
    @staticmethod
    def get(url, sid=None, headers=None):
        if headers is None:
            headers = {
                'Cookie': f'wps_sid={sid}'
            }
        info(f're url: {url}')
        info(f're headers: {json.dumps(headers)}')
        try:
            res = requests.get(url=url, headers=headers, timeout=3)
        except TimeoutError:
            error(f'{url} api requests timeout!')
            return 'timeout'
        info(f'res code: {res.status_code}')
        info(f'res body: {res.text}')
        return res
