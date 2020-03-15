"""
testboilerplate.py
====================================
The core module of my example project
"""

def about_me(your_name):
    """
    Return the most important thing about a person.
    Parameters
    ----------
    your_name
        A string indicating the name of the person.
    """
    return "The wise {} loves Python.".format(your_name)


class ExampleClass:
    """An example docstring for a class definition."""

    def __init__(self, name):
        """
        Blah blah blah.
        Parameters
        ---------
        name
            A string to assign to the `name` instance attribute.
        """
        self.name = name

    def about_self(self):
        """
        Return information about an instance created from ExampleClass.
        """
        return "I am a very smart {} object.".format(self.name)


class MyNewClass:
    """
    This class is mainly a test to see if it works.
    """
    def __init__(self, name: str = "Laksh"):
        """
        This Class is the demonstrate numpy docstring.
        Parameters
        ----------
        name
            This is supposed to be the name of the person.
        """
        self.name = name

    def greet(self):
        """
        Greets the user
        :return: string
        """
        return print("Hello" + self.name)
