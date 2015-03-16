import unittest
import sqlite3

from ..core.user.User import User
from ..core.user import UserAuthentication, UserRetrieval
from ..data.sqlite import UserDataStrategy

class TestUserDataStrategy(unittest.TestCase):
    def setUp(self):
        conn = sqlite3.connect("src/data/sqlite/staticcms.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("DELETE FROM users")
        conn.commit()
        conn.close()
    def tearDown(self):
        conn = sqlite3.connect("src/data/sqlite/staticcms.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("DELETE FROM users")
        conn.commit()
        conn.close()

    def testUserSaves(self):
        self.assertTrue(UserAuthentication.saveUser(User("test", "test@example.com"), "pass1234", UserDataStrategy))
        self.assertTrue(UserRetrieval.doesAUserExist(UserDataStrategy))
    def testUserAutheticationWorks(self):
        UserAuthentication.saveUser(User("test", "test@example.com"), "pass1234", UserDataStrategy)
        self.assertFalse(UserAuthentication.autheticateUser("test", "p1234", UserDataStrategy))
        self.assertTrue(UserAuthentication.autheticateUser("test", "pass1234", UserDataStrategy))


    def testDoesUserExistMethod(self):
        self.assertFalse(UserRetrieval.doesAUserExist(UserDataStrategy))


if __name__ == "__main__":
    unittest.main()
