from __future__ import annotations
import sqlite3
import bcrypt

class UserManager:
    """Handles everything related to user management"""

    def __init__(self, databaseLocation: str):
        self.db = databaseLocation

    def cursor(self) -> sqlite3.Cursor:
        return sqlite3.connect(self.db).cursor()
    
    def validateCredentials(self, username: str, password: str) -> bool:
        """Return true if the credentials are valid
        """
        qry = f"SELECT PASSWORD FROM CREDENTIALS WHERE USERNAME = '{username.strip()}'"
        success = False
        cursor = self.cursor()
        try:
            cursor.execute(qry)
            record = cursor.fetchone()

            if not record:
                raise self.UserNotFound(username)

            success = bcrypt.checkpw(password.encode(), record[0].encode())

        finally:
            cursor.close()

        return success
    
    def validateCredentialsDummy(self, username: str, password: str) -> bool:
        if password == "pass":
            return True
        else: return False
    
    class UserNotFound(Exception):
        """User does not exist in the database"""

        def __init__(self, username, *args):
            super().__init__(args)
            self.username = username

        def __str__(self):
            return f"{self.username} does not exist!"