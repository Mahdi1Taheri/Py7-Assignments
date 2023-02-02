
class Media:
    def __init__(self,name,director,imdb,url,duration):
        self.name = name
        self.director = director
        self.imdb_score = imdb
        self.url = url
        self.duration = duration
        self.casts = []

    def showInfo(self):
        ...
    
    def download(self):
        ...