import unittest
import sqlite3
from datetime import date

from ..core.posts.Post import Post
from ..core.posts import PostCRUD, PostRetrieval
from ..data.sqlite import PostDataStrategy

class TestPosDataStrategy(unittest.TestCase):
    def setUp(self):
        self.postObjecToTestA = Post("A sample post", """<p>The post body</p>\n[image 1 center]\n<p><p>The ending paragraph</p>""",
                date(2015,3,1), "a-sample-post")
        self.postObjecToTestB = Post("A sample poste", """<p>The post body</p>\n[image 1 center]\n<p><p>The ending paragraph</p>""",
                date(2015,3,1), "a-sample-poste")
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
        self.assertTrue(PostCRUD.savePost(self.postObjecToTestA, PostDataStrategy))

    def testMainPagePostsRetrieveCorrectly(self):
        PostCRUD.savePost(self.postObjecToTestA, PostDataStrategy)
        PostCRUD.savePost(self.postObjecToTestB, PostDataStrategy)
        posts = PostRetrieval.getMainPagePosts(10, PostDataStrategy)
        self.assertEqual(len(posts), 2)
    
    def testSinglePostRetrievesCorrectly(self):
        PostCRUD.savePost(self.postObjecToTestA, PostDataStrategy)
        PostCRUD.savePost(self.postObjecToTestB, PostDataStrategy)
        post = PostRetrieval.getSinglePost('a-sample-post', PostDataStrategy)
        self.assertEqual(post.postTitle, "A sample post")
        self.assertEqual(post.postUrl, "a-sample-post")

    def testAllPostsRetrieveCorrectly(self):
        PostCRUD.savePost(self.postObjecToTestA, PostDataStrategy)
        PostCRUD.savePost(self.postObjecToTestB, PostDataStrategy)
        allPosts = PostRetrieval.getPosts(PostDataStrategy)
        self.assertEqual(len(allPosts), 2)

if __name__ == "__main__":
    unittest.main()
