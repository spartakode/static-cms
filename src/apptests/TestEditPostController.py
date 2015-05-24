import unittest
from unittest.mock import Mock
from datetime import date

from ..controllers import EditPostController
from ..data import DataStrategy
from ..core.posts.Post import Post
from ..core.posts import PostCRUD

class TestEditPostController(unittest.TestCase):
    def setUp(self):
        self.singlePostToReturn = Post("A sample title", "<h1>Some title</h1><p>Some text</p>", date.today(), "a-sample-post")
        DataStrategy.initializeDataStrategy("sqllite")
        mockPostDataStrategy = Mock()
        mockPostDataStrategyArgs = {
            "getSinglePost.return_value":self.singlePostToReturn,
            "updatePost.return_value": True,
            "getMainPagePosts.return_value": [self.singlePostToReturn],
            "savePost.return_value": True,
                }
        mockPostDataStrategy.configure_mock(**mockPostDataStrategyArgs)
        DataStrategy.PostDataStrategy  = mockPostDataStrategy

    def test_postRetrievesInMarkDownCorrectly(self):
        testPost = EditPostController.getPostInMarkdown("a-sample-post")
        testBody = """# Some title

Some text

"""
        self.assertEqual(testBody, testPost.postBody)

    def test_postUpdates(self):
        PostCRUD.savePost(self.singlePostToReturn, DataStrategy.PostDataStrategy)
        testPostInfo = {"postbody":"#A sample post", "posttitle": "A sample title", "posturl": "a-new-post", "postlink": "", "oldposturl": "a-sample-post"}
        self.assertTrue(EditPostController.updatePost(testPostInfo))

if __name__=="__main__":
    unittest.main()
