class Post:
    def __init__(self, postTitle, postBody, postDate, postUrl, postLink=""):
        self.postTitle = postTitle
        self.postBody = postBody
        self.postDate = postDate
        self.postUrl = postUrl
        self.postLink = postLink
        if self.postLink.strip() == "":
            self.isLinkBlog = False
        else:
            self.isLinkBlog = True
