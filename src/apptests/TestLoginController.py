import unittest
import sqlite3

from ..controllers import LoginController, RegisterController

class TestUserRegistration(unittest.TestCase):
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
    def testUserLogin(self):
        testData = {'username': 'adnan', 
                'email': 'test@example.com',
                'password': 'pass1234'}
        loginData = {'username': 'adnan', 
                'password': 'pass123'}
        RegisterController.registerUser(testData)
        self.assertFalse(LoginController.loginUser(loginData))
        loginData['password'] = 'pass1234'
        self.assertTrue(LoginController.loginUser(loginData))
if __name__ == "__main__":
    unittest.main()

