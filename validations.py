import re
from databases import Databases


class Validations:
    # validation e-mail checking if the e-mail has valid patern before insert in the user table SQLITE
    @staticmethod
    def isValidEmail(email: str) -> bool:
        emailPatern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        isValid = re.match(emailPatern, email)

        if isValid:
            return True
        else:
            return False

    # validation e-mail checking if the e-mail exists in the user table SQLITE DATABASE
    @staticmethod
    def emailNotExists(email: str) -> bool:
        Databases.init_connection("exemple.db")
        conn = Databases.get_connection()
        cursor = Databases.get_cursor()
        emailCheck = email

        query = "SELECT email FROM user WHERE email = ?"
        cursor.execute(query, (emailCheck,))
        result = cursor.fetchall()
        conn.commit()

        return bool(result)
