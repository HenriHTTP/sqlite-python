from databases import Databases


class Movie:
    def __init__(self, title: str, year: int, genre: str):
        self._title = title
        self._year = year
        self._genre = genre

    # create a movie in SQLITE DATABSE
    def createMovie(self) -> dict:
        conn = Databases.get_connection()
        cursor = Databases.get_cursor()
        query = "INSERT INTO movies (title, release_year , genre) VALUES (?, ?, ?)"

        movie = {
            "title": self._title,
            "year": self._year,
            "genre": self._genre,
        }

        cursor.execute(query, (movie["title"], movie["year"], movie["genre"]))
        conn.commit()
        return movie

    # find all movies with equal name in SQLITE DATABSE
    @classmethod
    def findMovie(cls, name: str) -> list:
        conn = Databases.get_connection()
        cursor = Databases.get_cursor()
        query = "SELECT title, release_year, genre  FROM movies WHERE title LIKE ? OR genre LIKE ?"
        cursor.execute(query, ("%" + name + "%", "%" + name + "%"))

        result = cursor.fetchall()
        allMovies: list = []

        for data in result:
            movie = {"title": data[0], "year": data[1], "genre": data[2]}
            allMovies.append(movie)

        conn.commit()

        return allMovies

    # find all movies in SQLITE DATABSE
    @classmethod
    def findAllMovie(cls) -> list:
        conn = Databases.get_connection()
        cursor = Databases.get_cursor()
        query = "SELECT title, release_year, genre  FROM movies WHERE 1"

        cursor.execute(query)
        result = cursor.fetchall()
        allMovies: list = []

        for data in result:
            movie = {"title": data[0], "year": data[1], "genre": data[2]}
            allMovies.append(movie)

        conn.commit()
        return allMovies
