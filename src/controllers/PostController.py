import markdown
from datetime import date

from ..core.posts.Post import Post
from ..core.posts import PostCRUD
from ..data.sqlite import PostDataStrategy

def savePost(formData):
    datePosted = date.today()
    postBody = markdown.markdown(formData['postbody'])
    postToSave = Post(formData['posttitle'],
            postBody,
            datePosted,
            formData['posturl'],
            formData['postlink'])
    return PostCRUD.savePost(postToSave, PostDataStrategy)
