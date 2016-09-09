import unittest
import sqlite3
from unittest.mock import Mock

from ..controllers import ViewPostController
from ..data import DataStrategy

class TestViewPostController(unittest.TestCase):
    #def setUp(self):
        #self.postObjects = []
        #for i in range(0,30):
            #self.postObjects.append(Post("A sample post", """<p>The post body</p>\n[image 1 center]\n<p><p>The ending paragraph</p>""",
                #date(2015,3,1), "a-sample-post%d"%i))
        #mockPostDataStrategy = Mock()
        #mockPostDataStrategyAtts = {"getPosts.return_value": self.postObjects}
        #mockPostDataStrategy.configure_mock(mockPostDataStrategyAtts)
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
    def testAllPostsRetrieveCorrectly(self):
        self.assertEqual(ViewPostController.getAllPosts(), [])

if __name__ =="__main__":
    unittest.main()
