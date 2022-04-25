class User:
    """
    Class that generates new instances of users
    """
    user_list = []

    def __init__(self,username,password):
        '''
        __init__ method defines the property of the object

        Arg:
            username: new user username
            password: new user password
        '''
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method save user object in user_list
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        Deletes saved user from user list
        """
        User.user_list.remove(self)

    @classmethod
    def user_exist(cls,name):
        """
        Method that checks if a user exists from the user list.
        Args:
            name: name of user account to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        """
        for user in cls.user_list:
            if user.username == name:
                    return True

        return False

