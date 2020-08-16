import csv
from datetime import time

count = 0
valid_count = 0
for i in range(12):
    start = i*5000
    step = 5000
    if i==0:
        start +=1
    end = start+step

    name = "cites_" + str(start) + "_to_" + str(end) + ".csv"
    print("-------------------------------------------")
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
    print(nowTime)
    print(name)
    portion_count = 0
    portion_valid_count = 0
    try:
        with open(name, 'r', encoding='UTF-8') as f:
            reader = csv.reader(f)
            for row in reader:
                portion_count+=1
                if row[2]!="NaN":
                    portion_valid_count+=1
    except:
        continue

    count+=portion_count
    valid_count+=portion_valid_count
    print("portion count: ",end='')
    print(portion_count)
    print("portion valid count: ",end='')
    print(portion_valid_count)

print("-------------------------------------------")
nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
print(nowTime)
print("total count: ", end='')
print(count)
print("total valid count: ", end='')
print(valid_count)



