import sys
sys.path.append("../..")
from testcase_automaker.interface.http_params_generator import http_params_generator
from testcase_automaker.Utils import httptools
from ptest.plogger import preporter
import requests
import copy
import random


class http_tester(object):
    '''

    >>> tester = http_tester(url='http://www.baidu.com', method='get',\
                            parameters_structure={'name': {'type': 'string', 'value': '', 'iscompulsory': True},\
                                                  'phone': {'type': 'number', 'value': '', 'iscompulsory': True}})
    >>> type(tester.pre_send_params_list)
    <class 'list'>
    >>> type(random.choice(tester.pre_send_params_list))
    <class 'dict'>
    >>> type(tester.url_list_for_method_get)
    <class 'list'>
    >>> tester.url in random.choice(tester.url_list_for_method_get)
    True

    >>> tester = http_tester(url='http://www.baidu.com', method='get',parameters_structure={})
    >>> len(tester.url_list_for_method_get)
    1
    >>> tester.url_list_for_method_get[0] == tester.url
    True

    '''

    def __init__(self, url, method, parameters_structure=None, session=None, headers=None):

        self.url = url
        self.method = method
        self.parameters_structure = parameters_structure
        self.session = session
        self.headers = headers

        if session is None:
            self.session = requests.Session()

        if parameters_structure is None:
            self.parameters_structure = dict()

        if isinstance(self.parameters_structure, dict):
            params_generator = http_params_generator(parameters_structure=self.parameters_structure)
            params_generator.generate_params_list()
            self.pre_send_params_list = params_generator.generated_params_list
        else:
            self.pre_send_params_list = None
            raise Exception('parameters_structure is not a dict！')

        # 若方法为get, 则构建请求url列表
        if self.pre_send_params_list is not None and self.method.lower() == 'get':
            url_list = []
            if self.pre_send_params_list:
                for pre_send_params in self.pre_send_params_list:
                    url = copy.deepcopy(self.url)
                    url += '?'
                    for key, value in pre_send_params.items():
                        if value is not None:
                            url += str(key) + '=' + str(value) + '&'
                    url = url[0:(len(url) - 1)]
                    url_list.append(url)
            else:
                url_list.append(self.url)
            self.url_list_for_method_get = url_list

    # 执行测试, 目前依附于ptest测试框架
    def exec_test(self, assertion=None):
        self.returned_data = []
        if self.method.lower() == 'get':
            for url in self.url_list_for_method_get:
                preporter.info('\n\n正在请求: ' + url + '\n\n')
                self.returned_data.append(
                    httptools.request(url=url, method=self.method, session=self.session, headers=self.headers,
                                      assertion=assertion))
        else:
            if len(self.pre_send_params_list) > 0:
                for pre_send_params in self.pre_send_params_list:
                    preporter.info('\n\n正在请求: ' + self.url + '\n\n' + '当前请求参数: ' + str(pre_send_params) + '\n\n')
                    self.returned_data.append(
                        httptools.request(url=self.url, method=self.method, json_data=pre_send_params,
                                          session=self.session, headers=self.headers, assertion=assertion))
            else:
                preporter.info('\n\n正在请求: ' + self.url + '\n\n')
                self.returned_data.append(httptools.request(url=self.url, method=self.method,
                                                            session=self.session, headers=self.headers, assertion=assertion))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

