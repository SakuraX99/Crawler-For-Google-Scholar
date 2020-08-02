import time
import pandas as pd

from scholarly import scholarly
from fp.fp import FreeProxy

data = {"Title":[],
        "cites":[],
        "year":[]}


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


source_data = open("iclr_year_conf_title_author_url_biburl_final_2017-2019.txt")
line = source_data.readline()
while line:
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
    print("-------------------------------------------------")
    print(nowTime)
    line = source_data.readline()
    data_array = line.split(" ##### ")
    ret = get_articleInfo(data_array[2])
    print(ret)

    json_str = str(ret)
    json = eval(str)
    print(type(json))
    print(json["bib"]["cites"])
    data["Title"].append(json["bib"]["title"])
    data["cites"].append(json["bib"]["cites"])
    data["year"].append(json["bib"]["year"])

source_data.close()

df = pd.DataFrame(data,columns = [ "Title","cites","year"])
df.to_csv("./cites.csv",index=False,columns=[ "Title","cites","year"])