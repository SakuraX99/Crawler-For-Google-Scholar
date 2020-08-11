import time
import pandas as pd
import logging
import os
import sys
import csv
from scholarly import scholarly
from fp.fp import FreeProxy

def set_new_proxy():
    while True:
        proxy = FreeProxy(timeout=1, rand=True).get()
        proxy_works = scholarly.use_proxy(http=proxy, https=proxy)
        if proxy_works:
            break
    print("Working proxy:", proxy)
    return proxy

def get_articleInfo(title):
    while True:
        try:
            search_query = scholarly.search_pubs(title)
            print("Got the results of the query")
            break
        except Exception as e:
            print("Trying new proxy")
            set_new_proxy()

    pub = next(search_query)

    return pub

if __name__ == '__main__':

    start = eval(sys.argv[1])
    capacity = eval(sys.argv[2])
    tag = "cites/cites_" + str(start) + "_to_" + str(start + capacity) + ".csv"
    log_tag = "log/" + str(start) + "_to_" + str(start + capacity) + "_log.txt"

    logging.basicConfig(filename=os.path.join(os.getcwd(), log_tag), level=logging.DEBUG)

    # 存储读取的数据对象
    data = {"Title": [],
            "cites": [],
            "year": [],
            "abstract": []
            }

    # source_data = open("nlpedia-db.csv")
    # line = source_data.readline()

    with open('nlpedia-db.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)

        idx = 0


        for row in reader:

            idx+=1
            if idx>start and idx<=(start+capacity):
                nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
                print("-------------------------------------------------")
                print(nowTime)
                try:
                    ret = get_articleInfo(row[5])
                    print(ret)
                    json_str = str(ret)
                    json = eval(json_str)
                    print(type(json))
                    print(json["bib"]["cites"])
                    data["Title"].append(json["bib"]["title"])
                    data["cites"].append(json["bib"]["cites"])
                    data["year"].append(json["bib"]["year"])
                    data["abstract"].append(json["bib"]["abstract"])
                    df = pd.DataFrame(data, columns=["Title", "cites", "year"])
                    df.to_csv(tag, index=False, columns=["Title", "cites", "year"])
                except Exception as e:
                    logging.debug("fetch error:")
                    logging.debug(row[5])
                    data["Title"].append(row[5])
                    data["cites"].append("NaN")
                    data["year"].append(row[1])
                    data["abstract"].append("NaN")
                    df = pd.DataFrame(data, columns=["Title", "cites", "year"])
                    df.to_csv(tag, index=False, columns=["Title", "cites", "year"])

