import unittest
from unittest.mock import Mock
from datetime import date

from ..posts.Post import Post
from ..posts import PostCRUD, PostRetrieval

from ..statichtml.archivegeneration import ArchiveGenerator

class TestArchiveGenerator(unittest.TestCase):
    def setUp(self):
        self.postList = []
        self.postList.append(Post('january post 1 title',
            '<p>some january text</p>',
            date(2015, 1, 1),
            'january-post-1'))
        self.postList.append(Post('march post 1 title',
            '<p>some march text</p>',
            date(2015, 3, 1),
            'march-post-1'))
        self.mockPostDataStrategy = Mock()
        mockPostDataStrategyAttrs = {
                "getPosts.return_value": self.postList,
                }
        self.mockPostDataStrategy.configure_mock(**mockPostDataStrategyAttrs)
    def test_retrievingPostsForArchivesReturnsDictionaryCorrectly(self):
        dictionaryForTestArchive = ArchiveGenerator.getDictionaryForMainArchivePage(self.mockPostDataStrategy)
        dictionaryToTestAgainst = {'years':
                {'2015':{
                    'January':'201501',
                    'March':'201503',
                    }
                    }
                }
        self.assertEqual(dictionaryForTestArchive, dictionaryToTestAgainst)
    def test_archivePageGeneratorRunsCorrectly(self):
        archiveGeneratorResult = ArchiveGenerator.generateMainArchivePage(self.mockPostDataStrategy) 
        self.assertIsNotNone(archiveGeneratorResult)
        print(archiveGeneratorResult)
if __name__ == "__main__":
    unittest.main()