import configparser
from jinja2 import Environment, FileSystemLoader

from ..posts import PostRetrieval
def generateHtmlForPostPage(post):
    env = Environment(loader=FileSystemLoader('./src/core/templates/'))
    postTemplate = env.get_template('post-page.html')
    title = post.postTitle
    formattedPostDate = post.postDate.strftime('%B %d %Y')
    postConfigurations = getConfigurations()['POSTCONFIGURATIONS']
    return postTemplate.render(post=post,
            title=title,
            renderedPostBody=post.postBody,
            formattedPostDate = formattedPostDate,
            authorLink = postConfigurations['authorLink'],
            feedlyButtonInformation = postConfigurations['feedlyButtonInformation'],
            googleAnalyticsKey = postConfigurations['googleAnalyticsKey'],
            googleAnalyticsDomain = postConfigurations['googleAnalyticsDomain'],
            disqusShortName = postConfigurations['disqusShortName'])

def generateHtmlForMainPage(postDataStrategy):
    env = Environment(loader=FileSystemLoader('./src/core/templates/'))
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
