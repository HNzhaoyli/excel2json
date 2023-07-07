# coding:utf-8
from sklearn.metrics import accuracy_score, confusion_matrix
import json
import numpy as np
from predict_map_true import map_pred
from txt_compare import acc_txt

y_true_list=['商超百货-文玩店', '医药保健-药店', '汽修配件-汽车美容', '餐饮外卖-鲜啤店', '茶叶茶具-茶具', '生活服务-美容店', '生活服务-刻章店', '汽修配件-汽车维修', '商超百货-化妆品店', '茶叶茶具-茶馆', '宠物-宠物医院', '茶叶茶具-茶叶', '文体办公-画材绘画', '服装纺织-日用家纺', '蛋糕烘焙-甜点', '商超百货-玩具店', '宠物-宠物美容', '餐饮外卖-奶茶店', '蛋糕烘焙-蛋糕', '家居建材-机电电器', '商超百货-钟表店', '电子产品-电子数码', '文体办公-体育用品店', '汽修配件-汽车4s店', '服装纺织-箱包店', '医药保健-医疗器械', '家居建材-锁具', '商超百货-电子烟店', '服装纺织-服装店', '鲜花绿植-园艺用品店', '商超百货-珠宝首饰', '文体办公-乐器店', '家居建材-装修材料-美缝剂', '商超百货-精品店', '电子产品-家电', '商超百货-婚庆店', '汽修配件-汽车配件', '文体办公-打印店', '服装纺织-鞋店', '餐饮外卖-美食-火锅店', '果蔬生鲜-生鲜', '市场批发-农副产品批发-干货批发', '果蔬生鲜-水果店', '家居建材-装修材料-瓷砖地板', '餐饮外卖-美食-品牌快餐', '家居建材-装修材料-墙纸装饰', '家居建材-装修材料-油漆涂料', '商超百货-大型商超', '宠物-水族馆', '文体办公-书店', '市场批发-日用品批发', '餐饮外卖-美食-烧烤店', '生活服务-理发店', '商超百货-超市便利店', '医药保健-成人用品', '商超百货-眼镜店', '家居建材-装修材料-水暖管材', '家居建材-五金电工-五金配件', '鲜花绿植-鲜花绿植店', '医药保健-医院', '服装纺织-洗衣修鞋店', '果蔬生鲜-蔬菜店', '市场批发-生鲜批发', '商超百货-零食店', '文体办公-摄影文艺', '电子产品-电子维修', '宠物-宠物店', '家居建材-厨房卫浴', '汽修配件-汽车电子设备', '生活服务-快递行业', '电子产品-电脑办公', '商超百货-工艺品店', '家居建材-灯饰照明', '宠物-宠物用品', '商超百货-母婴店', '商超百货-烟酒店', '餐饮外卖-咖啡店', '餐饮外卖-美食-小龙虾', '家居建材-布艺家纺', '市场批发-农副产品批发-粮油调味', '餐饮外卖-美食-早餐店', '生活服务-配钥匙', '文体办公-文具店', '家居建材-五金电工-电工工具', '服装纺织-舞蹈服装']

y_true= []
y_pred=[]

print("original_acc:",acc_txt("generated_predictions_95.txt"))
# 读取txt文档
with open("generated_predictions_95.txt", 'r',encoding="utf-8") as file:
    for line in file:
        # 解析每一行的 JSON 对象
        json_object = json.loads(line)
        y_true.append(json_object["labels"])
        y_pred.append(json_object["predict"])


print(y_true,"\n",y_pred)
print(len(set(y_true)),"\n",len(set(y_pred)))

print("Ori_ml_acc:",accuracy_score(y_true,y_pred))

y_pred1 = map_pred(y_pred,y_true_list)
print(y_pred1)
print("map_pred:",len(set(y_pred1)))
# 计算预测精度

accuracy = accuracy_score(y_pred, y_pred1)
print("Accuracy_perd1_pred:", accuracy)
accuracy = accuracy_score(y_true, y_pred1)
print("Accuracy_map_pred:", accuracy)
# 生成混淆矩阵
cm = confusion_matrix(y_true, y_pred1)

print("Confusion Matrix:")
print(cm)
# 将混淆矩阵保存为文本文件
np.savetxt('confusion_matrix.txt', cm, fmt='%d')