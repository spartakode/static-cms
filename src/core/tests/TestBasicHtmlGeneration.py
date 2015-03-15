import unittest
from datetime import date

from ..statichtml import HtmlGenerator
from ..posts.Post import Post

class TestBasicHtmlGeneration(unittest.TestCase):
    def setUp(self):
        self.testPost = Post("A Sample Blog Post", "<p>A sample first paragraph</p>\n<p>A sample ending paragraph</p>", date(2015, 3, 3), "a-sample-post")
    def testPostPageHtmlGenerated(self):
        self.maxDiff = None
        samplePostFile = open('./src/core/tests/testdata/posts/posthtmlsample.html', 'r')
        samplePostHtml = samplePostFile.read()
        samplePostFile.close()
        postPageHtml = HtmlGenerator.generateHtmlForPostPage(self.testPost)
        self.assertEqual(postPageHtml, samplePostHtml)

if __name__=="__main__":
    unittest.main()
