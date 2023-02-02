from media import Media

class Film(Media):
    def __init__(self, name, director, imdb, url, duration, casts,genre, summary, year):
        super().__init__(name, director, imdb, url, duration, casts)
        self.genre = genre
        self.summary = summary
        self.year = year