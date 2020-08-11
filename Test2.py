

for i in range(112):
    Str = "nohup python3 -u Crawler_Parameter.py " + str(i*500) + " 500 > Crawler_" + str(i*500) +"_500.log 2>&1 &"
    print(Str)
