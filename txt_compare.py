import json

data1 = "generated_predictions.txt"
data2 = "generated_predictions_200.txt"

list1 = []
list2 = []
# 读取txt文档
with open(data1, 'r',encoding="utf-8") as file:
    for line in file:
        # 解析每一行的 JSON 对象
        json_object = json.loads(line)
        list1.append(json_object)

with open(data2, 'r', encoding="utf-8") as file:
    for line in file:
        # 解析每一行的 JSON 对象
        json_object = json.loads(line)
        list2.append(json_object)

i=0
j=0

for d1,d2 in zip(list1,list2):
    j=j+1
    if d1["predict"] == d2["predict"]:
        i=i+1
    else:
        print(d1["predict"],d2["predict"])
print("Acc:",i/j)


def acc_txt(txt):
    import json

    i = 0
    j = 0
    with open(txt, 'r', encoding="utf-8") as f:
        for line in f:
            line = json.loads(line)
            # 在此处对每一行进行处理
            j = j + 1
            if line["predict"] == line["labels"]:
                i = i + 1
            #if line["predict"] != line["labels"]:
                #print(line)
        acc = i/j
    return acc
