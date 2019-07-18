import urllib.request, json 


def get_photo(query):
     api_key = '13073520-7ecee33fd5cac057225dc2fb1'
     with urllib.request.urlopen(f"https://pixabay.com/api/?key={api_key}&q={query}+bird&category=animals&image_type=photo") as url:
        data = json.loads(url.read().decode())
        return data["hits"][0]["largeImageURL"]


def get_song(query):
    """return full name of bird and her song"""
    with urllib.request.urlopen("https://www.xeno-canto.org/api/2/recordings?query="+query) as url:
        data = json.loads(url.read().decode())
        song = data["recordings"][0]["en"], data["recordings"][0]["file"]
        return song[1] #.partition('www.xeno-canto.org')
    

def parse(sentence, stopwords):
    pass