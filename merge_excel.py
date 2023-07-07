import pandas as pd
import glob

# 获取文件夹下所有的Excel文件路径
file_paths = glob.glob('./merge_data/*.xlsx')

# 创建一个空的DataFrame来存储合并后的数据
merged_data = pd.DataFrame()

# 遍历每个Excel文件
for file_path in file_paths:
    # 读取Excel文件
    df= pd.read_excel(file_path)
    # 合并数据
    merged_data = pd.concat([merged_data, df], ignore_index=True)

# 保存合并后的数据为一个新的Excel文件
merged_data.to_excel('merged_data.xlsx', index=False)
