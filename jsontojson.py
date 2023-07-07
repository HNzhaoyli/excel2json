import pandas as pd
import json
import random

# # 读取Excel文件
#df = pd.read_excel('evl_data_new.json')
#
# # 组合两列数据为字典
# #data_dict = {}
# list = []
#for index, row in df.iterrows():
     #print(row)
#     #data_dict[row['address']] = row['label']
#     data_dict = {
#         'address': row['address'],
#         'label': row['label']
#     }
#     #data_dict = (row["address"],row["label"])
#     list.append(data_dict)
#
# # # 保存列表为JSON文件
# # with open('list_evl.json', 'w', encoding='utf-8') as f:
# #  json.dump(list, f,ensure_ascii=False)

# # 将列表保存为文件
# with open('evl_data_new.json', 'w', encoding='utf-8') as f:
#
#     for item in list:
#         json_data = json.dumps(item, ensure_ascii=False)
#         f.write(json_data)
#         #f.write(",")
#         f.write('\n')


list = []
# 读取JSON文件
with open('evl_data_new.json', 'r', encoding='utf-8') as f:
     #print(f)
     for line in f:
          # 解析每一行的 JSON 对象
          json_object = json.loads(line)
          list.append(json_object)
print(list)
# 将列表保存为文件
with open('evl_data_no_label.json', 'w', encoding='utf-8') as f:
    for item in list:
        data_dict = {
                     'address': item['address'],
                     'label': "NAN"
                 }
        json_data = json.dumps(data_dict, ensure_ascii=False)
        f.write(json_data)
        f.write('\n')


