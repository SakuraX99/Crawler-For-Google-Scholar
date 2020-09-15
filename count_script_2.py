import csv
import time
import os


count = 0
for root, dirs, files in os.walk("cites"):
    for f in files:
        portion_count = 0

        name = os.path.join(root, f)
        with open(name, 'r', encoding='UTF-8') as f:
            reader = csv.reader(f)
            for row in reader:
                portion_count += 1

            print(name)
            print(portion_count)
            count += portion_count

    print("total count:")
    print(count)