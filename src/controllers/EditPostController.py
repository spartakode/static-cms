from ..data import DataStrategy
import markdown
from ..core.posts.Post import Post
from ..core.posts import PostRetrieval
from ..core.posts import PostCRUD

def getPostInMarkdown(postUrlToRetrieve):
    return PostRetrieval.getSinglePostInMarkDown(postUrlToRetrieve, DataStrategy.PostDataStrategy)

def updatePost(postForm):
    originalPostUrl = postForm['oldposturl']
    postBody = markdown.markdown(postForm['postbody'])
    print(postBody)
    originalPost = PostRetrieval.getSinglePost(originalPostUrl, DataStrategy.PostDataStrategy)
    updatedPost = Post(postForm['posttitle'],
            postBody,
            originalPost.postDate,
            postForm['posturl'],
            postForm['postlink'])
    return PostCRUD.editPost(originalPostUrl, updatedPost, DataStrategy.PostDataStrategy)

def deletePost(deletePostForm):
    urlOfPostToDelete = deletePostForm['deleteposturl']
    return PostCRUD.deletePost(urlOfPostToDelete, DataStrategy.PostDataStrategy)
