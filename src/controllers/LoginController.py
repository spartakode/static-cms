from ..core.user.User import User
from ..core.user import UserAuthentication
from ..data.sqlite import UserDataStrategy
def loginUser(formData):
    return UserAuthentication.autheticateUser(formData['username'], formData['password'], UserDataStrategy)
