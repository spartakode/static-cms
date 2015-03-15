import unittest
from datetime import date

from ..posts.Post import Post

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

if __name__ == "__main__":
    unittest.main()
