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

# 井的数量
WELLLOG_NUM = 6

# 数据文件路径前缀
DATA_PREFIX = 'data/vertical_all_A{}.csv'

# 测试ID列表
TEST_ID = [6,]

# 目标列
COLUMNS_TARGET = ['HAC', 'BHC', 'DEN']

# 输入列
COLUMNS_INPUT = ['DEPT', 'RMN-RMG', 'CAL', 'SP', 'GR']

# 列描述
COLUMN_DESCRIPTIONS = {
    'DEPT': {
        'unit': 'm',
        'description': '深度，单位为米 (.M)'
    },
    'RMG': {
        'unit': 'ohmm',
        'description': '电阻率，单位为欧姆米 (.ohmm)'
    },
    'RMN': {
        'unit': 'ohmm',
        'description': '电阻率，单位为欧姆米 (.ohmm)'
    },
    'RMN-RMG': {
        'unit': 'ohmm',
        'description': '电阻率差值，没有明确单位，但由于是RMN与RMG的差值，其单位应该也是欧姆米 (.ohmm)'
    },
    'CAL': {
        'unit': 'cm',
        'description': '孔隙径，单位为厘米 (.cm)'
    },
    'SP': {
        'unit': 'mv',
        'description': '自发电位，单位为毫伏 (.mv)'
    },
    'GR': {
        'unit': 'API or unitless',
        'description': '伽马射线，单位未明确指出，但通常伽马射线的单位是API（美国石油学会单位）或者无单位'
    },
    'HAC': {
        'unit': 'us/m',
        'description': '声波时差，单位为微秒每米 (.us/m)'
    },
    'BHC': {
        'unit': 'us/m',
        'description': '表面声波时差，没有明确单位，可能是微秒每米 (.us/m)，因为与HAC类似'
    },
    'DEN': {
        'unit': 'g/cm3',
        'description': '密度，单位为克/立方厘米 (.g/cm3)'
    }
}

# 训练数据长度
TRAIN_LEN = 200

# 窗口步长
WINDOW_STEP = 100