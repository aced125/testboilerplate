"""Main module."""
class MyNewClass(object):
    def __init__(self, name: str = 'Laksh'):
        """
        My Class docs.
        :param name: Has to be a string.
        """
        self.name = name

    def greet(self):
        """
        Greets the user
        :return: string
        """
        return print("Hello" + self.name)
