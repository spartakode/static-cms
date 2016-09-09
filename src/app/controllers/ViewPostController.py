from ..data import DataStrategy
from ..core.posts import PostRetrieval

def getAllPosts():
    return PostRetrieval.getPosts(DataStrategy.PostDataStrategy)
