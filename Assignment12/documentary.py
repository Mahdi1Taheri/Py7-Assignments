from media import Media

class Documentary(Media):
    def __init__(self, name, director, imdb, url, duration, casts, episodes, genre, summary, trailer, year):
        super().__init__(name, director, imdb, url, duration, casts)
        self.episodes = episodes
        self.genre = genre
        self.summary = summary
        self.trailer = trailer
        self.year = year