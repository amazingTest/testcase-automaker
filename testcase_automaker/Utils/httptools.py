from ptest.assertion import assert_equals, fail
from ptest.plogger import preporter
import json


def request(url, method, json_data=None, session=None, headers=None, assertion=None):
    data = ''
    status_code = ''
    req_json = ''
    try:
        text = session.request(url=url, method=method, json=json_data, headers=headers).text
        if len(text) <= 1000:
            preporter.info(text)
        req_json = json.loads(text)
        status_code = req_json["status"]
        data = req_json["data"]
        preporter.info('接口返回status为:' + str(status_code))
        if len(str(data)) >= 3000:
            preporter.info('接口返回data为(限制长度为3000):' + str(data)[0:3000])
        else:
            preporter.info('接口返回data为:' + str(data))
    except BaseException:
        if not assertion:
            fail('无法获取status或data！')
        else:
            key = assertion.keys()
            assert_equals(assertion[key], req_json[key])
    finally:
        if not assertion:
            if not status_code == 'ok':
                preporter.error('接口响应:' + str(req_json))
            else:
                assert_equals(status_code, 'ok')
            assert_equals(status_code, 'ok')
        if data is not None:
            return data
