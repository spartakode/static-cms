from ..statichtml import HtmlGenerator

def savePost(postToSave, postDataStrategy):
    postSaveResult = postDataStrategy.savePost(postToSave)
    if postSaveResult:
        postPageHtml = HtmlGenerator.generateHtmlForPostPage(postToSave)
        mainPageHtml = HtmlGenerator.generateHtmlForMainPage(postDataStrategy)
        configurations = HtmlGenerator.getConfigurations()
        siteDirectory = configurations['SITEADMIN']['fileLocation']
        newPostFile = open(siteDirectory + '/posts/%s.html'%(postToSave.postUrl), 'wb')
        mainPageFile = open(siteDirectory + '/index.html', 'wb')
        newPostFile.write(postPageHtml.encode('utf-8'))
        newPostFile.close()
        mainPageFile.write(mainPageHtml.encode('utf-8'))
        mainPageFile.close()
        return True

    else:
        return False
