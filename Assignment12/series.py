from media import Media

class Series(Media):
    def __init__(self, name, director, imdb, url, duration, casts, episodes, season, guest_cast, genre,summary, trailer,year):
        super().__init__(name, director, imdb, url, duration, casts)
        self.episodes = episodes
        self.season = season
        self.guest_cast = guest_cast
        self.genre = genre
        self.summary = summary
        self.trailer = trailer
        self.year = year