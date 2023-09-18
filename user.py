from databases import Databases
from validations import Validations
import hashlib


class User:
    def __init__(self, username: str, password: str, email: str):
        self._username = username
        self._password = password
        self._email = email

    # method create a user in SQLITE DATABSE
    def createUser(self) -> dict:
        conn = Databases.get_connection()
        cursor = Databases.get_cursor()
        query = "INSERT INTO user (username, password, email) VALUES (?, ?, ?)"

        # email validations
        if not Validations.isValidEmail(self._email):
            return {"menssage": "Email is invalid"}

        if Validations.emailNotExists(self._email):
            return {"message": "Email already exists"}

        try:
            cryptPassword = hashlib.sha256(self._password.encode()).hexdigest()
            user = {
                "username": self._username,
                "password": cryptPassword,
                "email": self._email,
            }

            cursor.execute(query, (user["username"], user["password"], user["email"]))
            return user

        except Exception as err:
            return {"error": str(err)}

        finally:
            conn.commit()

    # method update user  per id in SQLITE DATABSE
    def updateUser(self, id: int, update: dict) -> dict:
        conn = Databases.get_connection()
        cursor = Databases.get_cursor()
        user = update
        query = "UPDATE user SET username = ?, email = ?  password = ? WHERE id = ?"

        cursor.execute(query, (user["username"], user["password"], user["email"], id))
        conn.commit()

        return user

    # method delete user per id in SQLITE DATABSE
    def deleteUser(self, id: int) -> dict:
        conn = Databases.get_connection()
        cursor = Databases.get_cursor()
        query = "DELETE FROM user WHERE id = ?"

        cursor.execute(query, (id))
        conn.commit()
        return {"message": f"Successfully deleted user with id {id} "}

    # method select one user SQLITE DATABASE
    def findOneUser(self, id: int) -> dict:
        conn = Databases.get_connection()
        cursor = Databases.get_cursor()
        query = "SELECT * FROM user WHERE id = ? "

        cursor.execute(query, (id,))
        data = cursor.fetchone()

        user: dict = {
            "id": data[0],
            "username": data[1],
            "password": data[2],
            "email": data[3],
        }
        conn.commit()
        return user

    # method select all users SQLITE DATABASE
    @classmethod
    def findAllUser(cls) -> list:
        conn = Databases.get_connection()
        cursor = Databases.get_cursor()
        query = "SELECT * FROM user WHERE 1"

        cursor.execute(query)
        result = cursor.fetchall()

        allUsers: list = []
        for data in result:
            register = {
                "id": data[0],
                "username": data[1],
                "password": data[2],
                "email": data[3],
            }
            allUsers.append(register)

        conn.commit()
        return allUsers
