import unittest
from unittest.mock import Mock

from ..user.User import User
from ..user import UserAuthentication, UserRetrieval

class TestUserCreation(unittest.TestCase):
    def setUp(self):
        self.mockUserDataStrategy = Mock()
        mockUserDataStrategyAttrs = {"saveUser.return_value": True,
                "getUserPasswordByUsername.return_value": "$2a$07$ArHGBK7IEdG0Q9Ps4TrsZOsy7NBaa3nwTV9XZ0oH.AkIAH2AN50dq",
                "doesAUserExist.side_effect": [False, True]}

        self.mockUserDataStrategy.configure_mock(**mockUserDataStrategyAttrs)

    def testUserSignUpWorksCorrectly(self):
        userToSave = User('testuser', 'test@example.com')
        self.assertTrue(UserAuthentication.saveUser(userToSave, 'pass1234', self.mockUserDataStrategy))
    def testUserLogsInCorrectly(self):
        self.assertTrue(UserAuthentication.autheticateUser('testuser', 'pass1234', self.mockUserDataStrategy))

    def testUserCountRetrievesCorrectly(self):
        self.assertFalse(UserRetrieval.doesAUserExist(self.mockUserDataStrategy))
        self.assertTrue(UserRetrieval.doesAUserExist(self.mockUserDataStrategy))

if __name__ == "__main__":
    unittest.main()
