import requests_with_caching
import json

def get_movies_from_tastedive(title):
    baseurl="https://tastedive.com/api/similar"
    parameter = {'q':title,'type':'movies','limit':"5"}
    tastedive = requests_with_caching.get(baseurl, params=parameter)
    taste_resp = json.loads(tastedive.text)
    return taste_resp 

#get_movies_from_tastedive("Bridesmaids")
#get_movies_from_tastedive("Black Panther")

def extract_movie_titles(diction):
    movie_list = []
    movies = diction['Similar']['Results']
    for movie in movies:
        movie_list.append(movie['Name'])
    return movie_list

#extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
#extract_movie_titles(get_movies_from_tastedive("Black Panther"))
def get_related_titles(list_of_movie):
    movie_list = []
    for title in list_of_movie:
        get_movies=get_movies_from_tastedive(title)
        extract_movies=extract_movie_titles(get_movies)
        for movie in extract_movies:
            if movie not in movie_list:
                movie_list.append(movie)
    return movie_list
#get_related_titles(["Black Panther", "Captain Marvel"])
#get_related_titles([])
def get_movie_data(title):
    parameter = {'t':title,'r':'json'}
    baseurl="http://www.omdbapi.com/"
    omdb = requests_with_caching.get(baseurl,parameter)
    omdb_resp=json.loads(omdb.text)
    return omdb_resp
#print(get_movie_data("Venom"))

def get_movie_rating(movie):
    rating = 0
    if len(movie['Ratings'])>1:
        if movie['Ratings'][1]['Source']=='Rotten Tomatoes':
            rating = movie['Ratings'][1]['Value'][:2]
            rating = int(rating)
    return rating

def getkey(item):
    return item[1]

def get_sorted_recommendations(list_of_movies):
    related_movies = get_related_titles(list_of_movies)
    ratings = list()
    sorted_list = list()
    for movie in related_movies:
        a = get_movie_data(movie)
        ratings.append(get_movie_rating(a))

    temp_tuple1 = zip(related_movies, ratings)
    temp_tuple2 = sorted(temp_tuple1, key=getkey, reverse=True)
    print(temp_tuple2)
    for i in range(len(temp_tuple2) - 1):
        if temp_tuple2[i][0] not in sorted_list:
            if temp_tuple2[i][1] == temp_tuple2[i + 1][1]:
                if temp_tuple2[i][0] < temp_tuple2[i + 1][0]:
                    sorted_list.append(temp_tuple2[i + 1][0])
                    sorted_list.append(temp_tuple2[i][0])
            else:
                sorted_list.append(temp_tuple2[i][0])

    print(sorted_list)

    return sorted_list

