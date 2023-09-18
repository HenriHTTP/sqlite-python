from databases import Databases
from user import User
from movie import Movie


if __name__ == "__main__":
    Databases.init_connection("exemple.db")
    Databases.close()
