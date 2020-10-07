import requests
import json
import asyncio
import websockets


def sort_data(response):

    DATA_SETS = ['title', 'year', 'rating', 'runtime',
                 'genres', 'mpa_rating', 'medium_cover_image', 'url', 'hash', 'type', 'seeds', 'peers', 'size']
    sorted_data = []
    response = json.loads(response)

    for key, value in response.items():
        if key == "data":
            data = value
    for key, value in data.items():
        if key == "movies":
            data = value
    for list_data in data:
        new_dict = {}
        data = list_data
        for key, value in data.items():
            if key in DATA_SETS:
                for x in DATA_SETS:
                    if x == key:
                        new_dict[x] = value
            if key == 'torrents':
                for y in value:
                    for key, value in y.items():
                        if key == 'quality':
                            quality = value
                            for key, value in y.items():
                                if key in DATA_SETS:
                                    new_dict[quality+'-'+str(key)] = value
                            new_dict['quality'] = quality
        sorted_data.append(new_dict)

    print(sorted_data)


def find_movie_api(search_query):

    url = "https://yts-am-torrent.p.rapidapi.com/list_movies.jsonp"

    querystring = {"query_term": search_query, "page": "1", "limit": "3"}

    headers = {
        'x-rapidapi-host': "yts-am-torrent.p.rapidapi.com",
        'x-rapidapi-key': "3feb6effb4mshbeb8c882b817831p15f8f0jsn781ee62cb9f0"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    response = response.text
    sort_data(response)


# while True:
    #search_query = input("Enter Movie:\n>>")
    # find_movie_api(search_query)
