import json


i = 0
j = 0
with open('generated_predictions_200.txt', 'r',encoding="utf-8") as f:
    for line in f:
        line = json.loads(line)
        # 在此处对每一行进行处理
        j = j+1
        if line["predict"]==line["labels"]:
            i=i+1
        if line["predict"]!=line["labels"]:
            print(line)

print(f"ACC:{i/j}%")

