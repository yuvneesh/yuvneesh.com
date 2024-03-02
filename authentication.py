from __future__ import annotations
import pyodbc
import bcrypt
import os

class UserManager:
    """Handles everything related to user management"""

    def __init__(self, connectionString: str):
        self.connectionString = connectionString
        print(self.connectionString)

    def cursor(self) -> pyodbc.Cursor:
        return pyodbc.connect(self.connectionString).cursor()
    
    def validateCredentials(self, username: str, password: str) -> bool:
        """Return true if the credentials are valid
        """
        qry = f"SELECT PASSWORD FROM LoginAppCreds WHERE USERNAME = '{username.strip()}'"
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