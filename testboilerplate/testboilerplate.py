"""Main module."""


class MyNewClass(object):
    def __init__(self, name: str = "Laksh"):
        """
        This Class implements naming.
        Args:
            name: A type of name, like Thom. Defaults to 'Laksh'.
        """
        self.name = name

    def greet(self):
        """
        Greets the user
        :return: string
        """
        return print("Hello" + self.name)
