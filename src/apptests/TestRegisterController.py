import unittest
import sqlite3

from ..controllers import RegisterController
from ..data import DataStrategy

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        DataStrategy.initializeDataStrategy("sqllite")
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
    def testUserRegistration(self):
        testData = {'username': 'adnan', 
                'email': 'test@example.com',
                'password': 'pass1234'}
        self.assertTrue(RegisterController.registerUser(testData))
if __name__ == "__main__":
    unittest.main()
