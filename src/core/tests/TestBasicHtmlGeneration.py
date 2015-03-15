import unittest
from unittest.mock import Mock
from datetime import date

from ..statichtml import HtmlGenerator
from ..posts.Post import Post

class TestBasicHtmlGeneration(unittest.TestCase):
    def setUp(self):
        self.testPost = Post("A Sample Blog Post", "<p>A sample first paragraph</p>\n<p>A sample ending paragraph</p>", date(2015, 3, 3), "a-sample-post")
        self.maxDiff = None
        self.postObjects = []
        for i in range(0,10):
            self.postObjects.append(Post("A sample post", """<p>The post body</p>\n[image 1 center]\n<p><p>The ending paragraph</p>""",
                date(2015,3,1), "a-sample-post%d"%i))
        self.mockProductDataStrategy = Mock()
        mockProductDataStrategyAttrs = {"savePost.return_value": True,
                "getMainPagePosts.return_value": self.postObjects}
        self.mockProductDataStrategy.configure_mock(**mockProductDataStrategyAttrs)

    def testConfigurationsRetrieveCorrectly(self):
        print(HtmlGenerator.getConfigurations())
        self.assertIsNotNone(HtmlGenerator.getConfigurations())
    def testPostPageHtmlGenerated(self):
        samplePostFile = open('./src/core/tests/testdata/posts/posthtmlsample.html', 'r')
        samplePostHtml = samplePostFile.read()
        samplePostFile.close()
        postPageHtml = HtmlGenerator.generateHtmlForPostPage(self.testPost)
        self.assertEqual(postPageHtml, samplePostHtml)

    def testMainPageHtmlGenerated(self):
        mainPageHtml = HtmlGenerator.generateHtmlForMainPage(self.mockProductDataStrategy)
        mainPageResultFile = open('./src/core/tests/testdata/mainpageresult.html', 'w')
        mainPageResultFile.write(mainPageHtml)
        mainPageResultFile.close()
        self.assertIsNotNone(mainPageHtml)
if __name__=="__main__":
    unittest.main()
