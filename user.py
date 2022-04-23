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