from cgi import test
from re import U
import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test case for User class behaviors

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test case
        """
        self.new_user = User("Clinton","comPlex!")

    def tearDown(self):
        """
        tearDown method cleans up after each test case
        """
        User.user_list = []

    def test_init(self):
        """
        test_init test case to test if object is intialized properly
        """

        self.assertEqual(self.new_user.username,"Clinton")
        self.assertEqual(self.new_user.password, "comPlex!")

    def test_save_user(self):
        """
        test_save_user test case checks if user object is saved in user list
        """
        self.new_user.save_user()
        print(User.user_list)
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users checks to see if multiple user objects can be added to user list
        """
        self.new_user.save_user()
        test_user = User("test username","test password")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        """
        test_delete_user checks if user can be removed from user list
        """
        self.new_user.save_user()
        test_user = User("Test username1","password1")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test user","pass")
        test_user.save_user()

        user_exists = User.user_exist("Test user")

        self.assertTrue(user_exists)

if __name__ == "__main__":
    unittest.main()
