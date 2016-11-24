import sqlite3
from datetime import date, timedelta

from ...core.posts.Post import Post
def savePost(postToSave):
    conn, cur = getConnectionAndCursor()
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
    conn, cur = getConnectionAndCursor()
    cur.execute("SELECT * FROM posts ORDER BY ROWID DESC LIMIT %d"%(postCount))
    results = cur.fetchall()
    postsToReturn = []
    return getPostsFromRows(results)

def getSinglePost(postUrl):
    conn, cur = getConnectionAndCursor()
    cur.execute("SELECT * FROM posts WHERE postUrl=:postUrl",{"postUrl":postUrl})
    result = cur.fetchone()
    postToReturn = None
    if result:
        postToReturn = convertPostRowToPostObject(result)
    return postToReturn

def getPosts():
    conn, cur = getConnectionAndCursor()
    cur.execute("SELECT * FROM posts ORDER BY postDate DESC")
    results = cur.fetchall()
    postsToReturn = []
    return getPostsFromRows(results)

def updatePost(oldPostUrl, updatedPost):
    conn, cur = getConnectionAndCursor()
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
    conn, cur = getConnectionAndCursor()
    cur.execute("DELETE FROM posts WHERE postUrl=:postUrl", {"postUrl": urlOfPostToDelete})
    conn.commit()
    conn.close()
    return True

def getPostsByYearAndMonth(year, month):
    conn, cur = getConnectionAndCursor()
    print(month)
    startDateOfMonth = date(year, month, 1)
    if month == 12:
        startDateOfNextMonth = date(year, 1, 1)
    else:
        startDateOfNextMonth = date(year, month + 1, 1)
    cur.execute("SELECT * FROM posts WHERE postDate >= :postDate AND postDate < :postDatePlusOneMonth ORDER BY ROWID DESC", {"postDate": startDateOfMonth.strftime('%Y-%m-%d'),
        "postDatePlusOneMonth": startDateOfNextMonth.strftime('%Y-%m-%d')})
    results = cur.fetchall()
    conn.close()
    return getPostsFromRows(results)

def convertPostRowToPostObject(postRow):
    dateParts = postRow['postDate'].split('-')
    postDate = (date(int(dateParts[0]), int(dateParts[1]), int(dateParts[2])))
    return Post(postRow['postTitle'],
            postRow['postBody'],
            postDate,
            postRow['postUrl'],
            postRow['postLink'])

def getPostsFromRows(rows):
    postsToReturn = []
    for row in rows:
        postsToReturn.append(convertPostRowToPostObject(row))
    return postsToReturn

def getConnectionAndCursor():
    conn = sqlite3.connect("app/data/sqlite/staticcms.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    return conn, cur
