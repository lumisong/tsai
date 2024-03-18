"""
文件名: constants.py
作者: lumisong
创建日期: 2024-03-07 20:29:42
最后更新日期: 2024-03-07 20:29:42
公司: XXX
功能:
这个文件包含了一些常量，这些常量在整个项目中都会用到。
"""

# constants.py
# files_descriptions.py

# 大庆油田数据集
# 井的头部信息
WELLLOG_HEAD = ['DEPT', 'RMG', 'RMN', 'RMN-RMG', 'CAL', 'SP', 'GR', 'HAC', 'BHC', 'DEN']


# 数据文件路径前缀
DATA_PREFIX = 'data/vertical_all_A{}.csv'

# 测试ID列表
TEST_ID = [6,]

# 目标列
COLUMNS_TARGET = ['HAC', 'BHC', 'DEN']

# 输入列
COLUMNS_INPUT = ['DEPT', 'RMN-RMG', 'CAL', 'SP', 'GR']

# 列描述# constants.py
# files_descriptions.py

# 井的数量
WELLLOG_NUM = 21

column_descriptions = {
    'WELL_NAME': {
        'type': 'str',
        'unit': 'none',
        'description': '井名，用于标识不同的油井。'
    },
    'DEPTH': {
        'type': 'float',
        'unit': 'm',
        'description': '井深，单位为米。'
    },
    'GR': {
        'type': 'float',
        'unit': 'API or unitless',
        'description': '伽马射线，单位为API（美国石油学会单位）或者无单位。'
    },
    'BS': {
        'type': 'float',
        'unit': 'inch',
        'description': 'BS，单位为厘米。'
    },
    'CALI': {
        'type': 'float',
        'unit': 'cm',
        'description': '钻孔隙径，单位为厘米。'
    },
    'ROP': {
        'type': 'float',
        'unit': 'm/h',
        'description': '泵送速率，单位为米/小时。'
    },
    'RHOB': {
        'type': 'float',
        'unit': 'g/cm3',
        'description': '泥浆密度，单位为克/立方厘米。'
    },
    'NPHI': {
        'type': 'float',
        'unit': 'none',
        'description': '油分数，单位为百分比。'
    },
    'RACEHM': {
        'type': 'float',
        'unit': 'm',
        'description': '油层高度，单位为米。'
    },
    'RACELM': {
        'type': 'float',
        'unit': 'm',
        'description': '油层厚度，单位为米。'
    },
    'RM': {
        'type': 'float',
        'unit': 'ohmm',
        'description': '电阻率，单位为欧姆米。'
    },
    'RD': {
        'type': 'float',
        'unit': 'ohmm',
        'description': '电阻率差值，单位为欧姆米。'
    },
    'PEF': {
        'type': 'float',
        'unit': 'none',
        'description': '泥浆效率，单位为百分比。'
    },
    'DT': {
        'type': 'float',
        'unit': 'us/m',
        'description': '声波时差，单位为微秒每米。'
    },
    'DTS': {
        'type': 'float',
        'unit': 'us/m',
        'description': '表面声波时差，单位为微秒每米。'
    },
    'VCARB': {
        'type': 'float',
        'unit': 'none',
        'description': '碳化碳含量，单位为百分比。'
    },
    'VSH': {
        'type': 'float',
        'unit': 'none',
        'description': '水分含量，单位为百分比。'
    },
    'PHIF': {
        'type': 'float',
        'unit': 'none',
        'description': '油分数，单位为百分比。'
    },
    'SW': {
        'type': 'float',
        'unit': 'none',
        'description': '水分含量，单位为百分比。'
    },
    'KLOGH': {
        'type': 'float',
        'unit': 'none',
        'description': '水分含量，单位为百分比。'
    },
    'KLOGV': {
        'type': 'float',
        'unit': 'none',
        'description': '油分数，单位为百分比。'
    },
    'SAND_FLAG': {
        'type': 'bool',
        'unit': 'none',
        'description': '是否为砂岩标志，True表示是砂岩，False表示不是。'
    },
    'CARB_FLAG': {
        'type': 'bool',
        'unit': 'none',
        'description': '是否为碳化碳标志，True表示是碳化碳，False表示不是。'
    },
    'COAL_FLAG': {
        'type': 'bool',
        'unit': 'none',
        'description': '是否为煤标志，True表示是煤，False表示不是。'
    }
}

# 训练数据长度
TRAIN_LEN = 200

# 窗口步长
WINDOW_STEP = 100