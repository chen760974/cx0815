import csv

person = [('xxx', 18, 193), ('yyy', 18, 182), ('zzz', 19, 185)]
# 表头
header = ['name', 'age', 'height']

with open('person.csv', 'w', encoding='utf-8') as file_obj:
    # 1:创建writer对象
    writer = csv.writer(file_obj)
    # 2:写表头
    writer.writerow(header)
    # 3:遍历列表，将每一行的数据写入csv
    for p in person:
        writer.writerow(p)
