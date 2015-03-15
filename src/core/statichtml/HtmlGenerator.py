import configparser
from jinja2 import Environment, FileSystemLoader

def generateHtmlForPostPage(post):
    env = Environment(loader=FileSystemLoader('./src/templates/'))
    postTemplate = env.get_template('post-page.html')
    title = post.postTitle
    formattedPostDate = post.postDate.strftime('%B %d %Y')
    configurations = getConfigurations()
    return postTemplate.render(post=post,
            title=title,
            renderedPostBody=post.postBody,
            formattedPostDate = formattedPostDate,
            authorLink = configurations['authorLink'],
            feedlyButtonInformation = configurations['feedlyButtonInformation'],
            googleAnalyticsKey = configurations['googleAnalyticsKey'],
            googleAnalyticsDomain = configurations['googleAnalyticsDomain'],
            disqusShortName = configurations['disqusShortName'])

def getConfigurations():
    config = configparser.ConfigParser()
    config.read("src/config.ini")
    return config['POSTCONFIGURATIONS']
