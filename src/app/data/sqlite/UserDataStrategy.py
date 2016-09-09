import sqlite3

def doesAUserExist():
    conn = sqlite3.connect("app/data/sqlite/staticcms.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT count(ROWID) FROM users")
    result = cur.fetchone()
    conn.close()
    return result[0] != 0

def saveUser(userToSave, password):
    conn = sqlite3.connect("app/data/sqlite/staticcms.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, email, password) VALUES (?,?,?)",
            (userToSave.username, userToSave.email, password))
    conn.commit()
    conn.close()
    return True

def getUserPasswordByUsername(username):
    conn = sqlite3.connect("app/data/sqlite/staticcms.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username=:username",{"username":username})
    result = cur.fetchone()
    conn.close()
    if result:
        return str(result[0], 'utf-8')
    else:
        return None
