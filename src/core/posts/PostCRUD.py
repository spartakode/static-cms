from ..statichtml import HtmlGenerator
import os

def savePost(postToSave, postDataStrategy):
    postSaveResult = postDataStrategy.savePost(postToSave)
    if postSaveResult:
        postPageHtml = HtmlGenerator.generateHtmlForPostPage(postToSave)
        mainPageHtml = HtmlGenerator.generateHtmlForMainPage(postDataStrategy)
        configurations = HtmlGenerator.getConfigurations()
        siteDirectory = configurations['SITEADMIN']['fileLocation']
        if not os.path.exists(siteDirectory):
            os.mkdir(siteDirectory)
            os.mkdir(os.path.join(siteDirectory, 'posts'))
        newPostFile = open(siteDirectory + '/posts/%s.html'%(postToSave.postUrl), 'wb')
        mainPageFile = open(siteDirectory + '/index.html', 'wb')
        newPostFile.write(postPageHtml.encode('utf-8'))
        newPostFile.close()
        mainPageFile.write(mainPageHtml.encode('utf-8'))
        mainPageFile.close()
        return True

    else:
        return False

def editPost(oldPostUrl, updatedPost, postDataStrategy):
    postUpdateResult = postDataStrategy.updatePost(oldPostUrl, updatedPost)
    if postUpdateResult:
        postPageHtml = HtmlGenerator.generateHtmlForPostPage(updatedPost)
        mainPageHtml = HtmlGenerator.generateHtmlForMainPage(postDataStrategy)
        configurations = HtmlGenerator.getConfigurations()
        siteDirectory = configurations['SITEADMIN']['fileLocation']
        if not os.path.exists(siteDirectory):
            os.mkdir(siteDirectory)
            os.mkdir(os.path.join(siteDirectory, 'posts'))
        newPostFile = open(siteDirectory + '/posts/%s.html'%(updatedPost.postUrl), 'wb')
        if oldPostUrl != updatedPost.postUrl:
            os.remove(os.path.join(siteDirectory, 'posts', '%s.html'%(oldPostUrl)))
        mainPageFile = open(siteDirectory + '/index.html', 'wb')
        newPostFile.write(postPageHtml.encode('utf-8'))
        newPostFile.close()
        mainPageFile.write(mainPageHtml.encode('utf-8'))
        mainPageFile.close()
        return True

    else:
        return False
        
