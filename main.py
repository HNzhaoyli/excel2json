import pandas as pd

categories = [
    "餐饮外卖",
    "蛋糕烘焙",
    "果蔬生鲜",
    "电子产品",
    "医药保健",
    "文体办公",
    "宠物",
    "鲜花绿植",
    "茶叶茶具",
    "汽修配件",
    "市场批发",
    "家居建材",
    "商超百货",
    "生活服务",
    "公司企业",
    "服装纺织"
]
for name in categories:

    # 读取Excel表格
    #name = "商超百货"
    df = pd.read_excel(f"./label_data_industry/{name}.xlsx")

    Column1 = "start_address"
    Column2 = "一级大类"
    Column3 = "Industry_二级"
    Column4 = "industry_三级"


    # 将后三列使用连字符串联起来
    df['Merged'] = df[Column2].astype(str) + '-' + df[Column3].astype(str) + '-' + df[Column4].astype(str)

    # 选择第一列和"Merged"列
    new_df = df[[Column1, 'Merged']]

    # 保存为新的Excel文件
    new_df.to_excel(f'./merge_data/{name}_new.xlsx', index=False)
