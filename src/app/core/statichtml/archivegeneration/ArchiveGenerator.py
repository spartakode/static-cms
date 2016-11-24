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
        #responsible for saying one or more posts exist in YEAR, MONTH 
        # eg 2016 january.
        # generates the link for the archive page so january 2016 would be
        # 201601.html
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

def generateArchivePageForGivenMonthAndYear(month, year, postDataStrategy):
    print(month)
    allPosts = PostRetrieval.getPostsByYearAndMonth(month, year, postDataStrategy)
    configurations = HtmlGenerator.getConfigurations()
    env = Environment(loader=FileSystemLoader(os.path.join('.','templates','custom')))
    postConfigurations = configurations['POSTCONFIGURATIONS']
    mainPageConfigurations = configurations['MAINPAGE']
    try:
        archivePage = env.get_template('archivepage.html')
    except TemplateNotFound:
        shutil.copy(os.path.join('.','templates','default','archivepage.html'),
                os.path.join('.','templates','custom','archivepage.html'))
        archivePage = env.get_template('archivepage.html')
        
    print(allPosts)
    return archivePage.render(posts = allPosts,
            feedlyButtonInformation = postConfigurations['feedlyButtonInformation'],
            googleAnalyticsKey = postConfigurations['googleAnalyticsKey'],
            googleAnalyticsDomain = postConfigurations['googleAnalyticsDomain'],
            disqusShortName = postConfigurations['disqusShortName'])
