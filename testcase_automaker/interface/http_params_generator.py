import sys
sys.path.append("../..")
from testcase_automaker.Utils.amazingutils import randoms
from allpairspy import AllPairs
import random
import copy


class http_params_generator(object):
    '''


    >>> params_generator = http_params_generator(parameters_structure={'name': {'type': 'string', 'value': '','range':['张三','李四'], 'iscompulsory': True},\
                                                                      'phone': {'type': 'number', 'value': '', 'iscompulsory': True},\
                                                                       'claimant': {'type': 'object', 'value': {'name': {'type': 'string', 'value': '', 'iscompulsory': True}\
                                                                        ,'phone': {'type': 'number', 'value': '', 'iscompulsory': True}}, 'iscompulsory': True},\
                                                                       'informations': {'type': 'array', 'value': [{'claimant': {'type': 'object', 'value': {'name': {'type': 'string', 'value': '', 'iscompulsory': True}\
                                                                        ,'phone': {'type': 'number', 'value': '', 'iscompulsory': True}}, 'iscompulsory': True}},\
                                                                       {'name': {'type': 'string', 'value': '', 'iscompulsory': True}}], 'iscompulsory': True}})

    >>> params_generator.get_params_num()
    7
    >>> params_generator.generate_params_list()
    >>> type(params_generator.generated_params_list)
    <class 'list'>
    >>> type(random.choice(params_generator.generated_params_list))
    <class 'dict'>
    >>> len(params_generator.generated_params_list)
    7

    >>> params_generator = http_params_generator(parameters_structure={})
    >>> params_generator.get_params_num()
    0
    >>> params_generator.generate_params_list()
    >>> type(params_generator.generated_params_list)
    <class 'list'>
    >>> len(params_generator.generated_params_list)
    0

    '''
    def __init__(self, parameters_structure, generated_params_list=None):
        self.parameters_structure = parameters_structure
        self.generated_params_list = generated_params_list

    # 生成参数组合列表
    def generate_params_list(self):
        parameters = http_params_generator.get_pairwise_list(self.get_params_num())
        params_usage_2d_list = []
        params_combo_list = []
        if len(parameters) > 1:
            for pairs in AllPairs(parameters):
                params_usage_2d_list.append(pairs)
            for params_usage_list in params_usage_2d_list:
                yield_params_usage_list = http_params_generator.yield_list(params_usage_list)
                raw_params_list = self.generate_params(parameters_usage_list=yield_params_usage_list)
                prepared_params_list = http_params_generator.get_value_dic(raw_params_list)
                params_combo_list.append(prepared_params_list)
        elif len(parameters) == 1:  # 当只有一个参数的时候第三方库ALLPAIRS不支持
            yield_params_usage_list_true = http_params_generator.yield_list([True])
            yield_params_usage_list_false = http_params_generator.yield_list([False])
            raw_params_list_true = self.generate_params(parameters_usage_list=yield_params_usage_list_true)
            prepared_params_list_true = http_params_generator.get_value_dic(raw_params_list_true)
            raw_params_list_false = self.generate_params(parameters_usage_list=yield_params_usage_list_false)
            prepared_params_list_false = http_params_generator.get_value_dic(raw_params_list_false)
            params_combo_list.append(prepared_params_list_true)
            params_combo_list.append(prepared_params_list_false)
        self.generated_params_list = params_combo_list

    # 生成参数
    def generate_params(self, parameters_usage_list, parameters_structure=None):
        if parameters_structure is None:
            parameters_structure = copy.deepcopy(self.parameters_structure)
        for key, attribute in parameters_structure.items():
            type_name = attribute['type']
            if type_name.lower() == 'object':
                self.generate_params(parameters_structure=attribute['value'],
                                     parameters_usage_list=parameters_usage_list)
                continue
            if type_name.lower() == 'array':
                for value in attribute['value']:
                    self.generate_params(parameters_structure=value,
                                         parameters_usage_list=parameters_usage_list)
                continue
            type_category = self.get_type_category(key)
            if 'range' in attribute and attribute['range']:
                generated_value = random.choice(attribute['range'])
            else:
                generated_value = self.get_parameter_random_value(type_name, type_category)

            if next(parameters_usage_list) or ('range' in attribute and attribute['range']):
                parameters_structure[key]['value'] = generated_value
            else:
                parameters_structure[key]['value'] = None
        return parameters_structure

    def get_params_num(self, parameters_structure=None, num=0):
        if parameters_structure is None:
            parameters_structure = copy.deepcopy(self.parameters_structure)
        for key, attribute in parameters_structure.items():
            type_name = attribute['type']
            if type_name.lower() == 'object':
                num += self.get_params_num(attribute['value'])
                continue
            if type_name.lower() == 'array':
                for value in attribute['value']:
                    num += self.get_params_num(value)
                continue
            else:
                num += 1
        return num

    # 比较两个字典部分是否相等
    @staticmethod
    def remove_duplicated_dict_in_list(dic_list):
        for dic in dic_list:
            pass

    @staticmethod
    def yield_list(input_list):
        for i in input_list:
            yield i

    @staticmethod
    def get_pairwise_list(params_num):
        parameters = []
        for i in range(params_num):
            parameters.append([True, False])
        return parameters

    # 返回仅提取输入字典值中的value的值作为当前键的值的字典
    @staticmethod
    def get_value_dic(dic):
        new_dic = dict()
        for key, attribute in dic.items():
            if attribute['type'].lower() == 'object':
                new_dic[key] = http_params_generator.get_value_dic(attribute['value'])
                continue
            if attribute['type'].lower() == 'array':
                new_dic[key] = []
                for value in attribute['value']:
                    new_dic[key].append(http_params_generator.get_value_dic(value))
                continue
            new_dic[key] = attribute['value']
        return new_dic

    # 根据键名生成数据类别
    @staticmethod
    def get_type_category(key):
        if key == 'phone':
            return 'chinese_mobile_phone'
        if key == 'name':
            return 'chinese_name'
        else:
            return 'default'

    # 根据数据类型以及数据类型的类别生成随机数据
    @staticmethod
    def get_parameter_random_value(type_name, type_category='default'):
        if type_name.lower() == 'boolean':
            return randoms.get_random_boolean()
        if type_name.lower() == 'number':
            return randoms.get_random_num(num_type=type_category)
        if type_name.lower() == 'string':
            return randoms.get_random_str(str_type=type_category)
        if type_name.lower() == 'date':
            return randoms.get_random_num(length=9)
        else:
            return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
