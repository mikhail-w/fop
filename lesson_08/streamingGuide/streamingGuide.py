class Movie:
    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def __str__(self):
        return self.get_title()

    def get_title(self):
        return self._title

    def get_genre(self):
        return self._genre

    def get_director(self):
        return self._director

    def get_year(self):
        return self._year


class StreamingService:
    def __init__(self, name):
        self._name = name
        self._catalog = {}

    def __str__(self):
        return f"Name"

    def get_name(self):
        return self._name

    def get_catalog(self):
        return self._catalog

    def add_movie(self, movie_obj):
        # print(movie_obj._title)
        self._catalog[movie_obj.get_title()] = movie_obj

    def delete_movie(self, movie):
        if movie.title in self._catalog:
            del self._catalog[movie.get_title]


class StreamingGuide:
    def __init__(self):
        self._streaming_services = []

    def add_streaming_service(self, service):
        self._streaming_services.append(service)

    def delete_streaming_service(self, name):
        if name in self._streaming_services:
            self._streaming_services.remove(name)

    def where_to_watch_movie(self, title):

        for i in self._streaming_services:
            print(i)

        first = f"{title}(){self._streaming_services}"
        return first


movie_1 = Movie("The Seventh Seal", "comedy", "Ingmar Bergman", 1957)
movie_2 = Movie("Home Alone", "tragedy", "Chris Columbus", 1990)
movie_3 = Movie("Little Women", "action thriller", "Greta Gerwig", 2019)
movie_4 = Movie("Galaxy Quest", "historical documents", "Dean Parisot", 1999)

stream_serv_1 = StreamingService("Netflick")
stream_serv_1.add_movie(movie_2)
print(stream_serv_1.get_catalog())

# stream_serv_2 = StreamingService("Hula")
# stream_serv_2.add_movie(movie_1)
# stream_serv_2.add_movie(movie_4)
# stream_serv_2.delete_movie("The Seventh Seal")
# stream_serv_2.add_movie(movie_2)

# stream_serv_3 = StreamingService("Dizzy+")
# stream_serv_3.add_movie(movie_4)
# stream_serv_3.add_movie(movie_3)
# stream_serv_3.add_movie(movie_1)

# stream_guide = StreamingGuide()
# stream_guide.add_streaming_service(stream_serv_1)
# stream_guide.add_streaming_service(stream_serv_2)
# stream_guide.add_streaming_service(stream_serv_3)
# stream_guide.delete_streaming_service("Hula")
# search_results = stream_guide.where_to_watch_movie("Little Women")
