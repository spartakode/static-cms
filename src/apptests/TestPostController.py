import unittest
import sqlite3

from ..controllers import PostController
from ..data import DataStrategy

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        DataStrategy.initializeDataStrategy("sqllite")
        conn = sqlite3.connect("src/data/sqlite/staticcms.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("DELETE FROM posts")
        conn.commit()
        conn.close()
    def tearDown(self):
        conn = sqlite3.connect("src/data/sqlite/staticcms.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("DELETE FROM posts")
        conn.commit()
        conn.close()
    def testSavePost(self):
        postFormData = {'postbody': 'Some blog post\r\n\r\nAnd more stuff over here\r\n\r\nYey multiline stuff', 'posturl': 'a-new-blog-post', 'postlink': 'http://facebook.com', 'posttitle': 'A New Blog Post'}
        self.assertTrue(PostController.savePost(postFormData))

if __name__ == "__main__":
    unittest.main()
