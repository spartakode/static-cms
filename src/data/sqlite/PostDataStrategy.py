import sqlite3
from datetime import date

from ...core.posts.Post import Post
def savePost(postToSave):
    conn = sqlite3.connect("src/data/sqlite/staticcms.db")
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
    conn = sqlite3.connect("src/data/sqlite/staticcms.db")
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
