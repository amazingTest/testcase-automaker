# testcase-automaker

+ [testcase-automaker 中文文档](https://github.com/amazingTest/testcase-automaker/blob/master/README_CN.md)

testcase-automaker can be used to create interface testcase with different params combo base on pairwise strategy.

## Installation
    
    pip install allpairspy
    pip install testcase-automaker
    
## Best practice

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

run the script then u may get output like this:

    [{'name': '李四', 'phone': 15746159038, 'claimant': {'name': '华蔹绍', 'phone': 15698064521}, 'informations': [{'claimant': {'name': '齐檠', 'phone': 18912976530}}, {'name': '翟伽硝'}]}, {'name': '张三', 'phone': None, 'claimant': {'name': None, 'phone': None}, 'informations': [{'claimant': {'name': None, 'phone': None}}, {'name': '莫僖烹'}]}, {'name': '李四', 'phone': 18557203961, 'claimant': {'name': None, 'phone': 13736054179}, 'informations': [{'claimant': {'name': None, 'phone': 18810456792}}, {'name': None}]}, {'name': '李四', 'phone': None, 'claimant': {'name': '浦农', 'phone': None}, 'informations': [{'claimant': {'name': '阴桎煅', 'phone': None}}, {'name': None}]}, {'name': '张三', 'phone': None, 'claimant': {'name': None, 'phone': 18238590241}, 'informations': [{'claimant': {'name': '弓肓', 'phone': None}}, {'name': None}]}, {'name': '张三', 'phone': 18265714928, 'claimant': {'name': '昝胀噎', 'phone': None}, 'informations': [{'claimant': {'name': '应兰仓', 'phone': None}}, {'name': None}]}, {'name': '李四', 'phone': None, 'claimant': {'name': '毋羹', 'phone': None}, 'informations': [{'claimant': {'name': None, 'phone': 15701289735}}, {'name': None}]}]

    Process finished with exit code 0

which is a list that contains the params combo base on pairwise and the given params structure

## Contact me

For information and suggestions you can contact me at 523314409@qq.com
