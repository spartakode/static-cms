import configparser
import os, shutil
from jinja2 import Environment, FileSystemLoader

from ..posts import PostRetrieval
def generateHtmlForPostPage(post):
    if not os.path.exists(os.path.join('.','templates','custom')):
        #os.mkdir(os.path.join('.','templates', 'custom'))
        shutil.copytree(os.path.join('.', 'templates', 'default'), os.path.join('.','templates','custom'))

    env = Environment(loader=FileSystemLoader(os.path.join('.','templates','custom')))
    postTemplate = env.get_template('post-page.html')
    title = post.postTitle
    formattedPostDate = post.postDate.strftime('%B %d %Y')
    postConfigurations = getConfigurations()['POSTCONFIGURATIONS']
    return postTemplate.render(post=post,
            title=title,
            renderedPostBody=post.postBody,
            authorLink = postConfigurations['authorLink'],
            feedlyButtonInformation = postConfigurations['feedlyButtonInformation'],
            googleAnalyticsKey = postConfigurations['googleAnalyticsKey'],
            googleAnalyticsDomain = postConfigurations['googleAnalyticsDomain'],
            disqusShortName = postConfigurations['disqusShortName'])

def generateHtmlForMainPage(postDataStrategy):
    if not os.path.exists(os.path.join('.','templates','custom')):
        #os.mkdir(os.path.join('.','templates', 'custom'))
        shutil.copy(os.path.join('.', 'templates', 'default'), os.path.join('.','templates','custom'))
    env = Environment(loader=FileSystemLoader(os.path.join('.','templates','custom')))
    mainPageTemplate = env.get_template('main-page.html')
    title = "Welcome to Adnan's Blog"
    configurations = getConfigurations()
    postConfigurations = configurations['POSTCONFIGURATIONS']
    mainPageConfigurations = configurations['MAINPAGE']
    mainPagePosts = PostRetrieval.getMainPagePosts(int(mainPageConfigurations['numberOfPosts']), postDataStrategy)
    for post in mainPagePosts:
        post.renderedPostBody = post.postBody
    return mainPageTemplate.render(title=title,
            posts = mainPagePosts,
            feedlyButtonInformation = postConfigurations['feedlyButtonInformation'],
            googleAnalyticsKey = postConfigurations['googleAnalyticsKey'],
            googleAnalyticsDomain = postConfigurations['googleAnalyticsDomain'],
            disqusShortName = postConfigurations['disqusShortName'])
    
def getConfigurations():
    config = configparser.ConfigParser()
    config.read("src/config.ini")
    return config
