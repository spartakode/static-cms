import os
import shutil
from collections import OrderedDict
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound

from ...posts import PostRetrieval
from .. import HtmlGenerator

def getDictionaryForMainArchivePage(postDataStrategy):
    allPosts = PostRetrieval.getPosts(postDataStrategy)
    postDictionary = OrderedDict({'years':{}})
    for post in allPosts:
        yearOfPost = post.postDate.strftime('%Y')
        monthOfPost = post.postDate.strftime('%B')
        numberMonth = post.postDate.strftime('%m')
        if yearOfPost not in postDictionary['years']:
            postDictionary['years'][yearOfPost] = OrderedDict({})
        if monthOfPost not in postDictionary['years'][yearOfPost]:
            postDictionary['years'][yearOfPost][monthOfPost]= yearOfPost+numberMonth
    return postDictionary

def generateMainArchivePage(postDataStrategy):
    postDictionary = getDictionaryForMainArchivePage(postDataStrategy)
    configurations = HtmlGenerator.getConfigurations()
    env = Environment(loader=FileSystemLoader(os.path.join('.','templates','custom')))
    postConfigurations = configurations['POSTCONFIGURATIONS']
    mainPageConfigurations = configurations['MAINPAGE']
    try:
        archiveTemplate = env.get_template('archivetemplate.html')
    except TemplateNotFound:
        shutil.copy(os.path.join('.','templates','default','archivetemplate.html'),
                os.path.join('.','templates','custom','archivetemplate.html'))
        archiveTemplate = env.get_template('archivetemplate.html')
        
    return archiveTemplate.render(archivedPosts = postDictionary,
            feedlyButtonInformation = postConfigurations['feedlyButtonInformation'],
            googleAnalyticsKey = postConfigurations['googleAnalyticsKey'],
            googleAnalyticsDomain = postConfigurations['googleAnalyticsDomain']
            )
