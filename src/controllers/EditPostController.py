from ..data import DataStrategy
from ..core.posts.Post import Post
from ..core.posts import PostRetrieval
from ..core.posts import PostCRUD

def getPostInMarkdown(postUrlToRetrieve):
    return PostRetrieval.getSinglePostInMarkDown(postUrlToRetrieve, DataStrategy.PostDataStrategy)

def updatePost(postForm):
    originalPostUrl = postForm['oldposturl']
    originalPost = PostRetrieval.getSinglePost(originalPostUrl, DataStrategy.PostDataStrategy)
    updatedPost = Post(postForm['posttitle'],
            postForm['postbody'],
            originalPost.postDate,
            postForm['posturl'],
            postForm['postlink'])
    return PostCRUD.editPost(originalPostUrl, updatedPost, DataStrategy.PostDataStrategy)
