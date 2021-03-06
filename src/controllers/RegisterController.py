from ..core.user.User import User
from ..core.user import UserAuthentication
from ..data import DataStrategy
def registerUser(formData):
    userToRegister = User(formData['username'], formData['email'])
    return UserAuthentication.saveUser(userToRegister, formData['password'], DataStrategy.UserDataStrategy)
