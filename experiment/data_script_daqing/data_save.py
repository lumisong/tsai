# data_saver.py

import h5py
import numpy as np
from constants import COLUMN_DESCRIPTIONS

class DataSaveStrategy:
    """
    数据保存策略的基类。
    """
    def save_data(self, data, filename, file_description):
        """
        保存数据的方法。
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
class AdvancedDataSaver(DataSaveStrategy):
    """
    高级的数据保存策
    """
    def save_data(self, data, filename, file_description):
        # 实现高级的数据保存逻辑
        with h5py.File(filename, 'w') as h5f:
            h5f.attrs['file_description'] = file_description
            for key in data.columns:
                dataset = h5f.create_dataset(key, data=data[key].values)
                if key in COLUMN_DESCRIPTIONS:
                    dataset.attrs['unit'] = COLUMN_DESCRIPTIONS[key]['unit']
                    dataset.attrs['description'] = COLUMN_DESCRIPTIONS[key]['description']
                    
class DefaultDataSaver(DataSaveStrategy):
    """
    默认的数据保存策略，使用data_save.py中的save_data_to_h5函数保存数据。
    """
    def save_data(self, data, filename, file_description):
        with h5py.File(filename, 'w') as h5f:
            h5f.attrs['file_description'] = file_description
            for key in data.columns:
                dataset = h5f.create_dataset(key, data=data[key].values)
                
def save_data_to_h5_using_strategy(data, filename, file_description, strategy=DefaultDataSaver()):
    strategy.save_data(data, filename, file_description)
    
# # 1. 默认数据保存策略
# # 导入必要的库
# import pandas as pd
# import h5py

# # 使用默认数据保存策略保存数据
# filename = "./well_log_daqing.h5"
# file_description = "这是一个示例文件。"
# data_saver = DefaultDataSaver()
# save_data_to_h5_using_strategy(df, filename, file_description, strategy=data_saver)
# print("数据已保存为well_log_daqing.h5。")

# # 2. 高级数据保存策略
# # 导入必要的库
# import pandas as pd
# import h5py

# # 使用高级数据加载策略加载数据
# filename = "./well_log_daqing.h5"
# file_description = "这是一个示例文件。"
# data_saver = AdvancedDataSaver()
# save_data_to_h5_using_strategy(df, filename, file_description, strategy=data_saver)
# print("数据已保存为well_log_daqing.h5。")
