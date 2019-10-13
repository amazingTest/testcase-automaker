# testcase-automaker

测试用例制造器，基于 pairwise 以及给定的参数结构自动生成用例参数组合。

## 安装

    pip install testcase-automaker
    
## 最佳实践

    from testcase_automaker.interface.http_params_generator import http_params_generator

    params_structure = {
                'name': {
                    'type': 'string',
                    'value': '',
                    'range': ['张三', '李四'],
                    'iscompulsory': True
                },
                'phone': {
                    'type': 'number',
                    'value': '',
                    'iscompulsory': True
                },
                'claimant': {
                    'type': 'object',
                    'value': {
                        'name': {
                            'type': 'string',
                            'value': '',
                            'iscompulsory': True
                        },
                        'phone': {
                            'type': 'number',
                            'value': '',
                            'iscompulsory': True
                        }
                    },
                    'iscompulsory': True
                },
                'informations': {
                    'type': 'array',
                    'value': [{
                            'claimant': {
                                'type': 'object',
                                'value': {
                                    'name': {
                                        'type': 'string',
                                        'value': '',
                                        'iscompulsory': True
                                    },
                                    'phone': {
                                        'type': 'number',
                                        'value': '',
                                        'iscompulsory': True
                                    }
                                },
                                'iscompulsory': True
                            }
                        },
                        {
                            'name': {
                                'type': 'string',
                                'value': '',
                                'iscompulsory': True
                            }
                        }
                    ],
                    'iscompulsory': True
                }
            }
    
    if __name__ == '__main__':
        params_generator = http_params_generator(parameters_structure=params_structure)
        params_list = params_generator.generate_params_list()
        print(params_generator.generated_params_list)

运行脚本后输出如下:

    [{'name': '李四', 'phone': 15746159038, 'claimant': {'name': '华蔹绍', 'phone': 15698064521}, 'informations': [{'claimant': {'name': '齐檠', 'phone': 18912976530}}, {'name': '翟伽硝'}]}, {'name': '张三', 'phone': None, 'claimant': {'name': None, 'phone': None}, 'informations': [{'claimant': {'name': None, 'phone': None}}, {'name': '莫僖烹'}]}, {'name': '李四', 'phone': 18557203961, 'claimant': {'name': None, 'phone': 13736054179}, 'informations': [{'claimant': {'name': None, 'phone': 18810456792}}, {'name': None}]}, {'name': '李四', 'phone': None, 'claimant': {'name': '浦农', 'phone': None}, 'informations': [{'claimant': {'name': '阴桎煅', 'phone': None}}, {'name': None}]}, {'name': '张三', 'phone': None, 'claimant': {'name': None, 'phone': 18238590241}, 'informations': [{'claimant': {'name': '弓肓', 'phone': None}}, {'name': None}]}, {'name': '张三', 'phone': 18265714928, 'claimant': {'name': '昝胀噎', 'phone': None}, 'informations': [{'claimant': {'name': '应兰仓', 'phone': None}}, {'name': None}]}, {'name': '李四', 'phone': None, 'claimant': {'name': '毋羹', 'phone': None}, 'informations': [{'claimant': {'name': None, 'phone': 15701289735}}, {'name': None}]}]

    Process finished with exit code 0

输出格式为数组，包含了基于 pairwise 的参数组合

## 联系我

可扫描下方二维码联系我

![2D-Code](https://github.com/amazingTest/Taisite-Platform/blob/master/images/微信公众号.jpg)    

## 捐赠

![2D-Code](https://github.com/amazingTest/Taisite-Platform/blob/master/images/wechatDonation.jpg)    
