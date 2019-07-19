import random
import urllib.request, json 

from textblob import TextBlob



def is_arabic(word):
    chars = "كلمنهويأإابتثجحخذدرزسشصضطظعغفق"
    if word[0] in chars:
        return True
    return False 


def translat(word, lang="en"):
    blob = TextBlob(word)
    word_trnaslated = blob.translate(to=lang)
    return str(word_trnaslated)


def get_photo(query):
    api_key = '13073520-7ecee33fd5cac057225dc2fb1'
    with urllib.request.urlopen(f"https://pixabay.com/api/?key={api_key}&q={query}+bird&category=animals&image_type=photo") as url:
        data = json.loads(url.read().decode())
        images = data["hits"]
        random_image = random.choice(images)
        return random_image["largeImageURL"]


def get_song(query):
    """return full name of bird and her song"""
    with urllib.request.urlopen("https://www.xeno-canto.org/api/2/recordings?query="+query) as url:
        data = json.loads(url.read().decode())
        recordings = data["recordings"]
        random_recording = random.choice(recordings)
        song = random_recording["en"], random_recording["file"]
        return song[1] #.partition('www.xeno-canto.org')
    

def parse(sentence, stopwords):
    pass