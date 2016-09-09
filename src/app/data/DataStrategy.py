from .sqlite import PostDataStrategy as SqlLitePostDataStrategy
from .sqlite import UserDataStrategy as SqlLiteUserDataStrategy

PostDataStrategy = None
UserDataStrategy = None

def initializeDataStrategy(dataType):
    global PostDataStrategy
    global UserDataStrategy
    if dataType == "sqllite":
        PostDataStrategy = SqlLitePostDataStrategy
        UserDataStrategy = SqlLiteUserDataStrategy
