# 1
"""import requests
import json
page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150])
print(page.url)
x = page.json() # page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x,indent=2))

# 2
kval_pairs = {'rel_rhy':'funny'}
page2 = requests.get("https://api.datamuse.com/words",params=kval_pairs)
print(page2.headers.keys())

# 3
import requests
def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {}
    params_diction['rel_rhy'] = word
    params_diction['max']='3' #get at most 3 results
    resp = requests.get(baseurl,params = params_diction)
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    return resp.json()
print(get_rhymes("funny"))
import requests
page = requests.get("https://www.google.com/search?tbm=isch&q=%20violins+and+guitars%20")
print(page.url)"""

#import requests_with_caching
#import json

#parameters = {"term": "Ann Arbor", "entity": "podcast"}
#iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params = parameters, permanent_cache_file="itunes_cache.txt")

#py_data = json.loads(iTunes_response.text)
#for r in py_data['results']:
#    print(r['trackName'])
"""
# import statements
import requests_with_caching
import json
# import webbrowser

# apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
# paste the key (not the secret) as the value of the variable flickr_key
flickr_key = 'yourkeyhere'

def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key # from the above global variable
    params_diction["tags"] = tags_string # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    flickr_resp = requests_with_caching.get(baseurl, params = params_diction, permanent_cache_file="flickr_cache.txt")
    # Useful for debugging: print the url! Uncomment the below line to do so.
    print(flickr_resp.url) # Paste the result into the browser to check it out...
    return flickr_resp.json()

result_river_mts = get_flickr_data("river,mountains")

# Some code to open up a few photos that are tagged with the mountains and river tags...

photos = result_river_mts['photos']['photo']
for photo in photos:
    owner = photo['owner']
    photo_id = photo['id']
    url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id)
    print(url)
    # webbrowser.open(url)
"""
    