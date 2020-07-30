from scholarly import scholarly

source_data = open("iclr_year_conf_title_author_url_biburl_final_2017-2019.txt")
line = source_data.readline()
while line:
    print(line)
    line = source_data.readline()
    data_array = line.split(" ##### ")
    print(data_array)

    search_query = scholarly.search_pubs(data_array[2])
    ret = next(search_query)


source_data.close()