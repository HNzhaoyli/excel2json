import numpy as np
from nltk.metrics.distance import edit_distance
import tqdm
# 真实标签
y_true = ['餐饮外卖-小龙虾', '餐饮外卖-早餐店', '餐饮外卖-奶茶店']

# 预测标签
y_pred = ['餐饮外卖-美食', '餐饮外卖-包子早餐', '餐饮外卖-coco奶茶',"餐饮外卖- "]

#
# # 计算相似度得分并改变预测标签
# for i in range(len(y_pred)):
#     pred_label = y_pred[i]
#     similarity_scores = [1 - edit_distance(pred_label, true_label) for true_label in y_true]
#     max_score_index = np.argmax(similarity_scores)
#     y_pred[i] = y_true[max_score_index]
#
# # 打印结果
# print(y_pred)

def map_pred(list_pred,list_true):
    # 计算相似度得分并改变预测标签
    #y_map_pred = []
    for i in range(len(list_pred)):
        pred_label = list_pred[i]
        similarity_scores = [1 - edit_distance(pred_label, true_label) for true_label in list_true]
        max_score_index = np.argmax(similarity_scores)
        list_pred[i] = list_true[max_score_index]
        #y_map_pred.append(list_pred[i])
    return list_pred

if __name__ =="__main__":
    print(map_pred(y_pred,y_true))
