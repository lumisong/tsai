"""
文件名: data_load.py
作者: lumisong
创建日期: 2024-03-07 20:53:06
最后更新日期: 2024-03-07 20:53:06
公司: XXX
功能:
这个文件包含了数据加载的策略。
"""
import pandas as pd
import h5py

class DataLoaderStrategy:
    """
    数据加载策略的基类。
    """
    def load_data(self, filename):
        """
        加载数据的方法。
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
class AdvancedDataLoader(DataLoaderStrategy):
    """
    高级的数据加载策略，使用其他方式加载数据。
    
    """
    def load_data(self, filename):
        # 实现高级的数据加载逻辑
        with h5py.File(filename, 'r') as h5f:
            file_description = h5f.attrs.get('file_description', 'No description')
            print(f"File Description: {file_description}")
            data_df = pd.DataFrame()
            for key in h5f.keys():
                dataset = h5f[key]
                data_df[key] = dataset[:]
                unit = dataset.attrs.get('unit', 'No unit')
                description = dataset.attrs.get('description', 'No description')
                print(f"{key}: Unit = {unit}, Description = {description}")
            data_df['WellName'] = data_df['WellName'].apply(lambda x: x.decode('utf-8'))
            return data_df
            
class DefaultDataLoader(DataLoaderStrategy):
    """
    默认的数据加载策略，使用data_read.py中的load_data_from_h5函数加载数据。
    """
    def load_data(self, filename):
        # 实现默认的数据加载逻辑
        with h5py.File(filename, 'r') as h5f:
            data = {key: h5f[key][()] for key in h5f.keys()}
            data_df = pd.DataFrame(data)
            data_df['WellName'] = data_df['WellName'].apply(lambda x: x.decode('utf-8'))
            return data_df
        
def load_data_from_h5(filename, strategy=DefaultDataLoader()):
    return strategy.load_data(filename)


# # 1. 默认数据加载策略
# # 导入必要的库
# import pandas as pd
# import h5py

# # 使用默认数据加载策略加载数据
# filename = "./well_log_daqing_standardized.h5"
# data_loader = DefaultDataLoader()
# df = load_data_from_h5(filename, strategy=data_loader)

# # 打印加载的数据
# print(df.head())

# # 1. 高级数据加载策略
# # 导入必要的库
# import pandas as pd
# import h5py

# # 使用高级数据加载策略加载数据
# filename = "./well_log_daqing.h5"
# data_loader = AdvancedDataLoader()
# df = load_data_from_h5(filename, strategy=data_loader)

# # 打印加载的数据和文件描述信息
# print(df.head())
# print(f"File Description: {file_description}")
