from ..statichtml import HtmlGenerator
import os, shutil
import filecmp

def savePost(postToSave, postDataStrategy):
    postSaveResult = postDataStrategy.savePost(postToSave)
    if postSaveResult:
        postPageHtml = HtmlGenerator.generateHtmlForPostPage(postToSave)
        mainPageHtml = HtmlGenerator.generateHtmlForMainPage(postDataStrategy)
        configurations = HtmlGenerator.getConfigurations()
        siteDirectory = configurations['SITEADMIN']['fileLocation']
        if not os.path.exists(siteDirectory):
            os.mkdir(siteDirectory)
        if not os.path.exists(os.path.join(siteDirectory, 'posts')):
            os.mkdir(os.path.join(siteDirectory, 'posts'))
        if not os.path.exists(os.path.join(siteDirectory, 'static')):
            os.mkdir(os.path.join(siteDirectory, 'static'))
            shutil.copytree(os.path.join('.', 'templates', 'custom', 'styles'), os.path.join(siteDirectory, 'static', 'stylesheets'))
        else:
            resultOfFileComparisonInCustomCSSAndCSSInSiteFolder = filecmp.cmpfiles(os.path.join('.', 'templates', 'custom', 'styles'),
                    os.path.join(siteDirectory, 'static', 'stylesheets'),
                    os.listdir(os.path.join('.', 'templates', 'custom', 'styles'))
                    )
            if resultOfFileComparisonInCustomCSSAndCSSInSiteFolder[1] or resultOfFileComparisonInCustomCSSAndCSSInSiteFolder[2]:
                shutil.rmtree(os.path.join(siteDirectory, 'static', 'stylesheets'))
                shutil.copytree(os.path.join('.', 'templates', 'custom', 'styles'), os.path.join(siteDirectory, 'static', 'stylesheets'))

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
        if not os.path.exists(os.path.join(siteDirectory, 'posts')):
            os.mkdir(os.path.join(siteDirectory, 'posts'))
        if not os.path.exists(os.path.join(siteDirectory, 'static')):
            os.mkdir(os.path.join(siteDirectory, 'static'))
            shutil.copytree(os.path.join('.', 'templates', 'custom', 'styles'), os.path.join(siteDirectory, 'static', 'stylesheets'))
        else:
            resultOfFileComparisonInCustomCSSAndCSSInSiteFolder = filecmp.cmpfiles(os.path.join('.', 'templates', 'custom', 'styles'),
                    os.path.join(siteDirectory, 'static', 'stylesheets'),
                    os.listdir(os.path.join('.', 'templates', 'custom', 'styles'))
                    )
            if resultOfFileComparisonInCustomCSSAndCSSInSiteFolder[1] or resultOfFileComparisonInCustomCSSAndCSSInSiteFolder[2]:
                shutil.rmtree(os.path.join(siteDirectory, 'static', 'stylesheets'))
                shutil.copytree(os.path.join('.', 'templates', 'custom', 'styles'), os.path.join(siteDirectory, 'static', 'stylesheets'))

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
        
def deletePost(urlOfPostToDelete, postDataStrategy):
    postDeleteResult = postDataStrategy.deletePost(urlOfPostToDelete)
    if postDeleteResult is True:
        configurations = HtmlGenerator.getConfigurations()
        siteDirectory = configurations['SITEADMIN']['fileLocation']
        deleteFilePath = os.path.join(siteDirectory, 'posts', urlOfPostToDelete + '.html')
        if os.path.exists(deleteFilePath):
            os.remove(deleteFilePath)
        return True
    else:
        return False
