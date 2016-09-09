import html2text

def getMainPagePosts(postCount, postDataStrategy):
    return postDataStrategy.getMainPagePosts(postCount)

def getSinglePost(postUrl, postDataStrategy):
    return postDataStrategy.getSinglePost(postUrl)

def getSinglePostInMarkDown(postUrl, postDataStrategy):
    postToReturn = getSinglePost(postUrl, postDataStrategy)
    postToReturn.postBody = html2text.html2text(postToReturn.postBody)
    return postToReturn

def getPosts(postDataStrategy):
    return postDataStrategy.getPosts()
