from media import Media

class Clip(Media):
    def __init__(self, name, director, imdb, url, duration, casts,genre, summary, trailer,year):
        super().__init__(name, director, imdb, url, duration, casts)
        self.genre = genre
        self.summary = summary
        self.trailer = trailer
        self.year = year