from ..core.user.User import User
from ..core.user import UserAuthentication
from ..data import DataStrategy
def loginUser(formData):
    return UserAuthentication.autheticateUser(formData['username'], formData['password'], DataStrategy.UserDataStrategy)
