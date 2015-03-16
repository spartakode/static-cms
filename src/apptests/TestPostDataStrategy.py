import unittest
import sqlite3
from datetime import date

from ..core.posts.Post import Post
from ..core.posts import PostCRUD, PostRetrieval
from ..data.sqlite import PostDataStrategy

class TestPosDataStrategy(unittest.TestCase):
    def setUp(self):
        self.postObjecToTest = Post("A sample post", """<p>The post body</p>\n[image 1 center]\n<p><p>The ending paragraph</p>""",
                date(2015,3,1), "a-sample-post")
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

    def testPostSavesCorrectly(self):
        self.assertTrue(PostCRUD.savePost(self.postObjecToTest, PostDataStrategy))

    def testMainPagePostsRetrieveCorrectly(self):
        PostCRUD.savePost(self.postObjecToTest, PostDataStrategy)
        posts = PostRetrieval.getMainPagePosts(10, PostDataStrategy)
        self.assertEqual(len(posts), 1)

if __name__ == "__main__":
    unittest.main()
