from fp.fp import FreeProxy
from scholarly import scholarly


def set_new_proxy():
    while True:
        proxy = FreeProxy().get()
        proxy_works = scholarly.use_proxy(http=proxy, https=proxy)
        if proxy_works:
            break
    print("Working proxy:", proxy)
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

while True:
    try:
        filled = pub.fill()
        print("Filled the publication")
        break
    except Exception as e:
        print("Trying new proxy")
        set_new_proxy()

print(filled)