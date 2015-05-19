import html2text

def getMainPagePosts(postCount, postDataStrategy):
    return postDataStrategy.getMainPagePosts(postCount)

def getSinglePost(postUrl, postDataStrategy):
    return postDataStrategy.getSinglePost(postUrl)

def getSinglePostInMarkDown(postUrl, postDataStrategy):
    postInHTML = getSinglePost(postUrl, postDataStrategy)
    postInMarkdown = html2text.html2text(postInHTML.postBody)
    return postInMarkdown
