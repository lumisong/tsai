# data

## 下载地址

案例：<https://zenodo.org/records/3902637>；

- zenodo：开发研究数据存储库(配合 github)。
- 唯一标识符：3902637，Appliances Energy Dataset。

## 数据集介绍

关键词：times series, energy, regression

家庭能源，预测一个房子的总能源使用量（以千瓦时为单位）。

数据集包含了138个时间序列，这些时间序列来自于UCI仓库的“Appliances Energy Prediction”数据集。[原始仓库](http://tseregression.org/)

时间序列的维度为24，包括9个房间的温度和湿度测量（通过ZigBee无线传感器网络监测），以及从Chievres机场测量的天气和气候数据，如温度、压力、湿度、风速、能见度和露点。

数据集是按照10分钟的平均周期进行的，覆盖了4.5个月的时间。

这个数据集的目标是通过分析这些时间序列数据来预测家庭的总能源使用量。这种预测可以帮助研究人员和工程师了解能源使用的模式，从而优化能源管理策略，例如调整使用时间或使用更高效的设备，以减少能源消耗。

数据集的创建者将UCI仓库的原始数据集转化为适合时间序列回归分析的格式。[数据处理细节链接](https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction)

相关的研究论文，如Luis M. Candanedo等人的“Data driven prediction models of energy use of appliances in a low-energy house”，这些论文可能提供了使用这个数据集进行研究的一些背景和方法。

总的来说，这个数据集是一个宝贵的资源，适合那些对家庭能源使用模式感兴趣的研究人员，或者希望通过分析时间序列数据来优化能源管理策略的工程师。

Files
Files (14.9 MB)
Name Size
AppliancesEnergy_TEST.ts
md5:e1f487613d7ad2ba2707c5bdd2d7c2a9 4.6 MB
AppliancesEnergy_TRAIN.ts
md5:311a605f24eab4f273e89de3eead7032 10.3 MB

根据您提供的详细信息，我创建了以下表格来整理和展示这个数据集的关键信息。

| 类别             | 详情                                                                                                                                     |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 数据集名称       | Appliances Energy Dataset                                                                                                              |
| 创建者           | Chang Wei Tan, Christoph Bergmeir, Francois Petitjean, Geoffrey I Webb                                                                 |
| 数据来源         | UCI仓库的“Appliances Energy Prediction”数据集                                                                                           |
| 目标             | 预测一个房子的总能源使用量（以千瓦时为单位）                                                                                                   |
| 时间序列数量     | 138个                                                                                                                                   |
| 时间序列维度     | 24维                                                                                                                                    |
| 监测内容         | 9个房间的温度和湿度测量（通过ZigBee无线传感器网络监测），以及从Chievres机场测量的天气和气候数据，如温度、压力、湿度、风速、能见度和露点                                     |
| 数据频率         | 10分钟平均周期                                                                                                                           |
| 数据覆盖时间     | 4.5个月                                                                                                                                  |
| 相关研究论文     | Luis M. Candanedo, Veronique Feldheim, Dominique Deramaix, "Data driven prediction models of energy use of appliances in a low-energy house", Energy and Buildings, Volume 140, 1 April 2017, Pages 81-97, ISSN 0378-7788 |
| 数据集下载       | Zenodo记录页面：<https://zenodo.org/records/3902637>                                                                                    |

## 相关数据

[2022 消费发电数据](https://zenodo.org/records/6778401)
