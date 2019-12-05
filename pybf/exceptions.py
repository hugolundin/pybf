class InputError(Exception):
    """Exception raised for invalid user input. 

    Attributes:
        value -- the value that was invalid. 
        message -- explanation of the error.
    """
    def __init__(self, value, message):
        self.value = value
        self.message = message

class TokenError(Exception):
    """Exception raised for invalid tokens. 

    Attributes:
        token -- the token that was invalid. 
        message -- explanation of the error.
    """
    def __init__(self, token, message):
        self.token = token
        self.message = message
