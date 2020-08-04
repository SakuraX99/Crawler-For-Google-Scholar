from scholarly import scholarly

scholarly.use_proxy(http="http://123.179.163.100:53954", https="https://123.179.163.100:53954")
search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
print("Got the results of the query")
pub = next(search_query)
print(pub)