import unittest
import sqlite3
from datetime import date

from ..core.posts.Post import Post
from ..core.posts import PostCRUD, PostRetrieval
from ..data import DataStrategy
from ..data.sqlite import PostDataStrategy

class TestPostDataStrategy(unittest.TestCase):
    def setUp(self):
        DataStrategy.initializeDataStrategy("sqllite")
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

    def testPostUpdatesCorrectly(self):
        PostCRUD.savePost(self.postObjecToTestA, PostDataStrategy)
        self.postObjecToTestA.postBody = "#A new World"
        self.postObjecToTestA.postTitle = "A new title"
        self.postObjecToTestA.postUrl = "a-new-url"
        self.postObjecToTestA.postLink = "thing-can-change"
        PostCRUD.editPost("a-sample-post", self.postObjecToTestA, PostDataStrategy)
        updateTestResult = PostRetrieval.getSinglePostInMarkDown("a-new-url", PostDataStrategy)
        self.assertEqual(updateTestResult.postTitle, "A new title")
        self.assertEqual(updateTestResult.postUrl, "a-new-url")
        self.assertEqual(updateTestResult.postLink, "thing-can-change")
        self.assertEqual(updateTestResult.postBody, "#A new World\n\n")

    def testPostDeletesCorrectly(self):
        PostCRUD.savePost(self.postObjecToTestA, PostDataStrategy)
        self.assertEqual(len(PostRetrieval.getMainPagePosts(10, PostDataStrategy)),1)
        PostCRUD.deletePost("a-sample-post", PostDataStrategy)
        self.assertEqual(len(PostRetrieval.getMainPagePosts(10, PostDataStrategy)),0)
if __name__ == "__main__":
    unittest.main()
