import configparser
import os, shutil
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import PyRSS2Gen as RSS2

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
    generateRss(mainPagePosts)
    return mainPageTemplate.render(title=title,
            posts = mainPagePosts,
            feedlyButtonInformation = postConfigurations['feedlyButtonInformation'],
            googleAnalyticsKey = postConfigurations['googleAnalyticsKey'],
            googleAnalyticsDomain = postConfigurations['googleAnalyticsDomain'],
            disqusShortName = postConfigurations['disqusShortName'])

def generateRss(posts):
    pageTitle = "Adnan Issadeen Meets Blogging"
    pageLink = "http://adnanissadeen.com"
    pageDescription = "The blog from the world of adnan issadeen"
    pageLastBuildDate= datetime.now()
    
    items = []
    for post in posts:
        title = post.postTitle
        if post.postLink:
            link = post.postLink + " &#8594;"
            permaLink = False
        else:
            link = "http://adnanissadeen.com/%s.html"%(post.postUrl)
            permaLink = True
        items.append(RSS2.RSSItem(
            title = title,
            link = link,
            description = post.postBody,
            guid = RSS2.Guid(link, permaLink),
            pubDate = datetime(post.postDate.year,
                post.postDate.month,
                post.postDate.day),
            )
        )
    rss = RSS2.RSS2(
                title=pageTitle,
                link = pageLink,
                description = pageDescription,
                lastBuildDate = pageLastBuildDate,

                items = items
            )
    configurations = getConfigurations()
    siteDirectory = configurations['SITEADMIN']['fileLocation']
    rss.write_xml(open(os.path.join(siteDirectory, "pyrss2gen.xml"), "w"))

def getConfigurations():
    config = configparser.ConfigParser()
    config.read("src/config.ini")
    return config
