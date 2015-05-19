import unittest
from unittest.mock import MagicMock, Mock
from datetime import date

from ..posts.Post import Post
from ..posts import PostCRUD, PostRetrieval

class TestPostObject(unittest.TestCase):
    def testPostObjectCreatedCorrectly(self):
        postObjecToTest = Post("A sample post", """<p>The post body</p>\n[image 1 center]\n<p><p>The ending paragraph</p>""",
                date(2015,3,1), "a-sample-post")
        self.assertEqual(postObjecToTest.postTitle, "A sample post")
        self.assertEqual(postObjecToTest.postBody, """<p>The post body</p>\n[image 1 center]\n<p><p>The ending paragraph</p>""")
        self.assertEqual(postObjecToTest.postDate, date(2015, 3, 1))
        self.assertEqual(postObjecToTest.postUrl, "a-sample-post")
        self.assertEqual(postObjecToTest.postLink, "")
        self.assertEqual(postObjecToTest.isLinkBlog, False)

class TestPostCRUD(unittest.TestCase):
    def setUp(self):
        self.postObjecToTest = Post("A sample post", """<p>The post body</p>\n<img src="someplace" alt="an image">\n<p>The ending paragraph</p>""",
                date(2015,3,1), "a-sample-post")
        self.postObjects = []
        for i in range(0,10):
            self.postObjects.append(Post("A sample post", """<p>The post body</p>\n[image 1 center]\n<p><p>The ending paragraph</p>""",
                date(2015,3,1), "a-sample-post%d"%i))
        self.mockProductDataStrategy = Mock()
        mockProductDataStrategyAttrs = {"savePost.return_value": True,
                "getMainPagePosts.return_value": self.postObjects,
                "getSinglePost.return_value": self.postObjecToTest,
                }
        self.mockProductDataStrategy.configure_mock(**mockProductDataStrategyAttrs)

    def testPostSavesCorrectly(self):
        self.assertTrue(PostCRUD.savePost(self.postObjecToTest, self.mockProductDataStrategy))

    def testMainPagePostsRetrieveCorrectly(self):
        self.assertEqual(PostRetrieval.getMainPagePosts(20, self.mockProductDataStrategy), self.postObjects)

    def testSinglePostRetrievesCorrectly(self):
        self.assertEqual(PostRetrieval.getSinglePost('a-sample-post', self.mockProductDataStrategy), self.postObjecToTest)

    def testSinglePostRetrievesMarkdownCorrectly(self):
        markDownToCompareTo = 'The post body\n\n![an image](someplace)\n\nThe ending paragraph\n\n'
        self.assertEqual(PostRetrieval.getSinglePostInMarkDown('a-sample-post', self.mockProductDataStrategy), markDownToCompareTo)

if __name__ == "__main__":
    unittest.main()
