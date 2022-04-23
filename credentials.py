class Credential:
    """
    Class that generates new instances of credentials
    """

    credentials_list = []

    def __init__(self,name, password, email):
        """
        __init__ method defines property of credentail object

        Arg:
            username: new credential name
            password: new credentail password
            email: new credential email
        """

        self.name = name
        self.password = password
        self.email = email

