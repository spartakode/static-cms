import unittest
from unittest.mock import MagicMock, Mock
from datetime import date

from ..posts.Post import Post
from ..posts import PostCRUD, PostRetrieval

class TestPostObject(unittest.TestCase):
    def testPostObjectCreatedCorrectly(self):
        postObjectToTest = Post("A sample post", """<p>The post body</p>\n[image 1 center]\n<p><p>The ending paragraph</p>""",
                date(2015,3,1), "a-sample-post")
        self.assertEqual(postObjectToTest.postTitle, "A sample post")
        self.assertEqual(postObjectToTest.postBody, """<p>The post body</p>\n[image 1 center]\n<p><p>The ending paragraph</p>""")
        self.assertEqual(postObjectToTest.postDate, date(2015, 3, 1))
        self.assertEqual(postObjectToTest.postUrl, "a-sample-post")
        self.assertEqual(postObjectToTest.postLink, "")
        self.assertEqual(postObjectToTest.isLinkBlog, False)

class TestPostCRUD(unittest.TestCase):
    def setUp(self):
        self.postObjectToTest = Post("A sample post", """<p>The post body</p>\n<img src="someplace" alt="an image">\n<p>The ending paragraph</p>""",
                date(2015,3,1), "a-sample-post")
        self.postObjects = []
        for i in range(0,30):
            self.postObjects.append(Post("A sample post", """<p>The post body</p>\n[image 1 center]\n<p><p>The ending paragraph</p>""",
                date(2015,3,1), "a-sample-post%d"%i))
        self.mockPostDataStrategy = Mock()
        mockProductDataStrategyAttrs = {"savePost.return_value": True,
                "getMainPagePosts.return_value": self.postObjects[0:20],
                "getPosts.return_value": self.postObjects,
                "getSinglePost.return_value": self.postObjectToTest,
                "updatePost.return_value": True,
                }
        self.mockPostDataStrategy.configure_mock(**mockProductDataStrategyAttrs)

    def testPostSavesCorrectly(self):
        self.assertTrue(PostCRUD.savePost(self.postObjectToTest, self.mockPostDataStrategy))

    def testMainPagePostsRetrieveCorrectly(self):
        self.assertEqual(PostRetrieval.getMainPagePosts(20, self.mockPostDataStrategy), self.postObjects[0:20])

    def testAllPostsRetrieveCorrectly(self):
        self.assertEqual(PostRetrieval.getPosts(self.mockPostDataStrategy), self.postObjects)
    def testSinglePostRetrievesCorrectly(self):
        self.assertEqual(PostRetrieval.getSinglePost('a-sample-post', self.mockPostDataStrategy), self.postObjectToTest)

    def testSinglePostRetrievesMarkdownCorrectly(self):
        markDownToCompareTo = 'The post body\n\n![an image](someplace)\n\nThe ending paragraph\n\n'
        self.assertEqual(PostRetrieval.getSinglePostInMarkDown('a-sample-post', self.mockPostDataStrategy), markDownToCompareTo)

    def testPostCanBeUpdated(self):
        self.postObjectToTest.postUrl = "an-edited-post"
        self.postObjectToTest.postLink = "http://example.com"
        self.assertTrue(PostCRUD.editPost("a-sample-post", self.postObjectToTest, self.mockPostDataStrategy))

if __name__ == "__main__":
    unittest.main()
