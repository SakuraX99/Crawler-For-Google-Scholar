

# for i in range(112):
#     Str = "nohup python3 -u Crawler_Parameter.py " + str(i*500) + " 500 > Crawler_" + str(i*500) +"_500.log 2>&1 &"
#     print(Str)
import csv
filename = 'pdf_get.sh'
with open(filename, 'w') as file_object:
    with open('nlpedia-db.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)

        idx = 0

        for row in reader:
            idx+=1
            if idx>1:
                url0 = row[7]
                url = url0.split(" ")[0]
                if url!="None":

                    print("wget " + url)
                    file_object.write("wget " + url +"\n")