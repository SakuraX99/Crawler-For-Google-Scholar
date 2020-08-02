from fp.fp import FreeProxy
from scholarly import scholarly
import json


def set_new_proxy():
    while True:
        proxy = FreeProxy().get()
        proxy_works = scholarly.use_proxy(http="http://103.197.46.131:8080", https="http://103.197.46.131:8080")
        if proxy_works:
            break
    print("Working proxy:", "http://103.197.46.131:8080")
    return proxy


set_new_proxy()

while True:
    try:
        search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
        print("Got the results of the query")
        break
    except Exception as e:
        print("Trying new proxy")
        set_new_proxy()

pub = next(search_query)
print(pub)

json = str(pub)
print("--------------------------")
print(json)
print("==========================")
print(type(json))
print("==========================")
json1 = json.loads(json)
print(json1)
print(type(json1))
print(json1["cites"])