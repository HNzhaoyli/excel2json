import pandas as pd
import json
import random

# 读取Excel文件
df = pd.read_excel('test_data_1000.xlsx')

# 组合两列数据为字典
#data_dict = {}
list = []
for index, row in df.iterrows():
    print(row)
    #data_dict[row['address']] = row['label']
    data_dict = {
        'address': row['address'],
        'label': row['label']
    }
    #data_dict = (row["address"],row["label"])
    list.append(data_dict)

# # 保存列表为JSON文件
# with open('list_evl.json', 'w', encoding='utf-8') as f:
#  json.dump(list, f,ensure_ascii=False)

# 将列表保存为文件
with open('test_data_10001.json', 'w', encoding='utf-8') as f:
    for item in list:
        json_data = json.dumps(item, ensure_ascii=False)
        f.write(json_data)
        #f.write(",")
        f.write('\n')


#
# # 读取JSON文件
# with open('evl_data.json', 'r', encoding='utf-8') as f:
#     data_all = json.load(f)
#     print(data_all)



