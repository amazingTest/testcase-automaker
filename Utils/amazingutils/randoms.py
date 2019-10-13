# -*- coding: UTF-8 -*-
import string
import random

def get_random_phone_num():
    num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
           '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
    start = random.choice(num_start)
    end = ''.join(random.sample(string.digits, 8))
    phone_num = start+end
    return phone_num


def get_random_chinese_word():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    random_chinese_word = bytes.fromhex(val).decode('gbk')
    return random_chinese_word


def get_random_str(length=8, str_type='default'):
    if str_type.lower() == 'default':
        random_str = ''.join(random.sample(string.ascii_letters + string.digits, length))
        return str(random_str)
    if str_type.lower() == 'chinese_word':
        random_chinese_word = []
        for i in range(length):
            random_chinese_word.append(get_random_chinese_word())
        return ''.join(random_chinese_word)
    if str_type.lower() == 'chinese_name':
        chinese_last_name_list = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '粱', '杜', '阮', '蓝', '闵', '席', '季', '麻', '强', '贾', '路', '娄', '危', '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '钟', '徐', '邱', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍', '虞', '万', '支', '柯', '昝', '管', '卢', '莫', '经', '房', '裘', '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓', '郁', '单', '杭', '洪', '包', '诸', '左', '石', '崔', '吉', '钮', '龚', '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁', '荀', '羊', '於', '惠', '甄', '麴', '家', '封', '芮', '羿', '储', '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫', '乌', '焦', '巴', '弓', '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬', '全', '郗', '班', '仰', '秋', '仲', '伊', '宫', '宁', '仇', '栾', '暴', '甘', '钭', '厉', '戎', '祖', '武', '符', '刘', '景', '詹', '束', '龙', '叶', '幸', '司', '韶', '郜', '黎', '蓟', '薄', '印', '宿', '白', '怀', '蒲', '邰', '从', '鄂', '索', '咸', '籍', '赖', '卓', '蔺', '屠', '蒙', '池', '乔', '阴', '欎', '胥', '能', '苍', '双', '闻', '莘', '党', '翟', '谭', '贡', '劳', '逄', '姬', '申', '扶', '堵', '冉', '宰', '郦', '雍', '舄', '璩', '桑', '桂', '濮', '牛', '寿', '通', '边', '扈', '燕', '冀', '郏', '浦', '尚', '农', '温', '别', '庄', '晏', '柴', '瞿', '阎', '充', '慕', '连', '茹', '习', '宦', '艾', '鱼', '容', '向', '古', '易', '慎', '戈', '廖', '庾', '终', '暨', '居', '衡', '步', '都', '耿', '满', '弘', '匡', '国', '文', '寇', '广', '禄', '阙', '东', '殴', '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂', '晁', '勾', '敖', '融', '冷', '訾', '辛', '阚', '那', '简', '饶', '空', '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯', '相', '查', '後', '荆', '红', '游', '竺', '权', '逯', '盖', '益', '桓', '公', '万俟', '司马', '上官', '欧阳', '夏侯', '诸葛', '闻人', '东方', '赫连', '皇甫', '尉迟', '公羊', '澹台', '公冶', '宗政', '濮阳', '淳于', '单于', '太叔', '申屠', '公孙', '仲孙', '轩辕', '令狐', '钟离', '宇文', '长孙', '慕容', '鲜于', '闾丘', '司徒', '司空', '亓官', '司寇', '仉', '督', '子车', '颛孙', '端木', '巫马', '公西', '漆雕', '乐正', '壤驷', '公良', '拓跋', '夹谷', '宰父', '谷梁', '晋', '楚', '闫', '法', '汝', '鄢', '涂', '钦', '段干', '百里', '东郭', '南门', '呼延', '归', '海', '羊舌', '微生', '岳', '帅', '缑', '亢', '况', '后', '有', '琴', '梁丘', '左丘', '东门', '西门', '商', '牟', '佘', '佴', '伯', '赏', '南宫', '墨', '哈', '谯', '笪', '年', '爱', '阳', '佟']
        random_chinese_name = []
        random_chinese_name.append(random.choice(chinese_last_name_list))
        for i in range(random.choice([1, 2])):
            random_chinese_name.append(get_random_chinese_word())
        return ''.join(random_chinese_name)


def get_random_num(length=8, num_type='default', eliminated_nums=None):
    if length < 1:
        raise ValueError
    if eliminated_nums is None:
        eliminated_nums = []
    if num_type.lower() == 'chinese_mobile_phone':
        return int(get_random_phone_num())
    num_list = list(map(int, list(string.digits)))
    for num in eliminated_nums:
        num_list.remove(num)
    seed = num_list
    random_num = []
    for i in range(length):
        random_num.append(random.choice(seed))
    if num_type.lower() == 'default':
        return int(''.join([str(num) for num in random_num]))


def get_random_boolean():
    random_boolean = random.choice([True, False])
    return random_boolean


if __name__ == '__main__':
    print(get_random_num(length=5, eliminated_nums=[0,1,2,3,4,5]))
    print(get_random_str(str_type='chinese_word'))
    print(get_random_str(str_type='chinese_name'))
    print(get_random_boolean())

