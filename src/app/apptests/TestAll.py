import unittest

from ..core.tests.TestPost import TestPostObject, TestPostCRUD
from ..core.tests.TestUser import TestUserCreation
from ..core.tests.TestBasicHtmlGeneration import TestBasicHtmlGeneration
from .TestLoginController import TestUserLogin
from .TestRegisterController import TestUserRegistration
from .TestUserDataStrategy import TestUserDataStrategy
from .TestViewPostController import TestViewPostController
from .TestPostDataStrategy import TestPostDataStrategy
from .TestPostController import TestPostController
from .TestEditPostController import TestEditPostController

if __name__ == "__main__":
    unittest.main()
