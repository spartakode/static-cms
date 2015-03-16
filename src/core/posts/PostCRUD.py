from ..statichtml import HtmlGenerator

def savePost(postToSave, postDataStrategy):
    postSaveResult = postDataStrategy.savePost(postToSave)
    if postSaveResult:
        postPageHtml = HtmlGenerator.generateHtmlForPostPage(postToSave)
        mainPageHtml = HtmlGenerator.generateHtmlForMainPage(postDataStrategy)
        configurations = HtmlGenerator.getConfigurations()
        siteDirectory = configurations['SITEADMIN']['fileLocation']
        newPostFile = open(siteDirectory + '/posts/%s.html'%(postToSave.postUrl), 'w')
        mainPageFile = open(siteDirectory + '/index.html', 'w')
        newPostFile.write(postPageHtml)
        newPostFile.close()
        mainPageFile.write(mainPageHtml)
        mainPageFile.close()
        return True
    else:
        return False
