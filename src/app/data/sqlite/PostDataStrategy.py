import sqlite3
from datetime import date

from ...core.posts.Post import Post
def savePost(postToSave):
    conn = sqlite3.connect("app/data/sqlite/staticcms.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""INSERT INTO posts (postTitle,
            postBody,
            postDate,
            postUrl,
            postLink) VALUES (?,?,?,?,?)""",
            (postToSave.postTitle,
                postToSave.postBody,
                postToSave.postDate,
                postToSave.postUrl,
                postToSave.postLink))
    conn.commit()
    conn.close()
    return True

def getMainPagePosts(postCount):
    conn = sqlite3.connect("app/data/sqlite/staticcms.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts ORDER BY ROWID DESC LIMIT %d"%(postCount))
    results = cur.fetchall()
    postsToReturn = []
    for result in results:
        dateParts = result['postDate'].split('-')
        postDate = (date(int(dateParts[0]), int(dateParts[1]), int(dateParts[2])))
        postsToReturn.append(Post(result['postTitle'],
            result['postBody'],
            postDate,
            result['postUrl'],
            result['postLink']))
    return postsToReturn

def getSinglePost(postUrl):
    conn = sqlite3.connect("app/data/sqlite/staticcms.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE postUrl=:postUrl",{"postUrl":postUrl})
    result = cur.fetchone()
    postToReturn = None
    if result:
        dateParts = result['postDate'].split('-')
        postDate = (date(int(dateParts[0]), int(dateParts[1]), int(dateParts[2])))
        postToReturn = Post(result['postTitle'],
            result['postBody'],
            postDate,
            result['postUrl'],
            result['postLink'])
    return postToReturn

def getPosts():
    conn = sqlite3.connect("app/data/sqlite/staticcms.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts ORDER BY postDate DESC")
    results = cur.fetchall()
    postsToReturn = []
    for result in results:
        dateParts = result['postDate'].split('-')
        postDate = (date(int(dateParts[0]), int(dateParts[1]), int(dateParts[2])))
        postsToReturn.append(Post(result['postTitle'],
            result['postBody'],
            postDate,
            result['postUrl'],
            result['postLink']))
    return postsToReturn

def updatePost(oldPostUrl, updatedPost):
    conn = sqlite3.connect("app/data/sqlite/staticcms.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE postUrl=:postUrl", {"postUrl": oldPostUrl})
    oldPost = cur.fetchone()
    if oldPost:
        cur.execute("UPDATE posts SET postTitle=:postTitle WHERE postUrl=:postUrl",{"postTitle": updatedPost.postTitle, "postUrl": oldPostUrl})
        cur.execute("UPDATE posts SET postBody=:postBody WHERE postUrl=:postUrl",{"postBody": updatedPost.postBody, "postUrl": oldPostUrl})
        cur.execute("UPDATE posts SET postLink=:postLink WHERE postUrl=:postUrl",{"postLink": updatedPost.postLink, "postUrl": oldPostUrl})
        cur.execute("UPDATE posts SET postUrl=:newPostUrl WHERE postUrl=:postUrl",{"newPostUrl": updatedPost.postUrl, "postUrl": oldPostUrl})
    conn.commit()
    conn.close()
    return True

def deletePost(urlOfPostToDelete):
    conn = sqlite3.connect("app/data/sqlite/staticcms.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("DELETE FROM posts WHERE postUrl=:postUrl", {"postUrl": urlOfPostToDelete})
    conn.commit()
    conn.close()
    return True
