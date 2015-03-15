import bcrypt

SALT_LENGTH = 29
WORK_FACTOR = 7

def getHashedPassword(password):
    return bcrypt.hashpw(password, bcrypt.gensalt(WORK_FACTOR))
def getSaltedHashedPasword(password, salt):
    return bcrypt.hashpw(password, salt)
def matchPassWord(password, hashedPassword):
    return hashedPassword == getSaltedHashedPasword(password, hashedPassword[:SALT_LENGTH])

def saveUser(userToSave, password, dataStrategy):
    hashedPassword = getHashedPassword(bytes(password, 'utf-8'))
    return dataStrategy.saveUser(userToSave, password)

def autheticateUser(username, password, dataStrategy):
    userPassword = dataStrategy.getUserPasswordByUsername(username)
    if userPassword:
        return matchPassWord(bytes(password, 'utf-8'), bytes(userPassword, 'utf-8'))
    else:
        return False
