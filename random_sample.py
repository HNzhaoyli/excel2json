import pandas as pd
import json
import random

#print(len(pd.read_json("evl_data_new.json")))
#print(len(pd.read_json("train_data_new.json")))
with open('evl_data_new.json', 'r',encoding='utf-8') as f:
    data = json.load(f)

# 获取数据个数
print(len(data))


# # 读取Excel表格
# df = pd.read_excel('merge_data_76.xlsx')
# #df = pd.read_json("lei_data.json")
# # 随机抽取部分数据
# sample_size = 1000  # 指定抽样大小
# sample_df = df.sample(n=sample_size)
#
# # 将抽样数据转换为字典列表
# sample_data = sample_df.to_dict(orient='records')
# print(sample_data)
# # 保存抽样数据为JSON文件
# with open('evl.json', 'w', encoding='utf-8') as f:
#     for data_dict in sample_data:
#         json_data = json.dumps(data_dict, ensure_ascii=False)
#         f.write(json_data)
#         #f.write(",")
#         f.write('\n')


# # 读取Excel表格数据
# df = pd.read_excel('merge_data_76.xlsx')
#
# # 获取数据总数
# total_count = len(df)

# # 随机抽取1000个数据
# random_indices = random.sample(range(total_count), 1000)
# df_selected = df.iloc[random_indices]
#
# # 获取剩下的数据
# df_remaining = df.drop(random_indices)
#
# # 将抽样数据转换为字典列表
# sample_data = df_selected.to_dict(orient='records')
# remain_data = df_remaining.to_dict(orient='records')
# # 保存抽样数据为JSON文件
# with open('evl_data_new.json', 'w', encoding='utf-8') as f:
#     for data_dict in sample_data:
#         json_data = json.dumps(data_dict, ensure_ascii=False)
#         f.write(json_data)
#         #f.write(",")
#         f.write('\n')
# with open('train_data_new.json', 'w', encoding='utf-8') as f:
#     for data_dict in remain_data:
#         json_data = json.dumps(data_dict, ensure_ascii=False)
#         f.write(json_data)
#         #f.write(",")
#         f.write('\n')

