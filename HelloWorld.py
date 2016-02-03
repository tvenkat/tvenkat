class HelloWorld:
    """
    hello world to python
    """

    def __init__(self):
        print "Hello World!"
        self.version = '2.7'

    def welcome(self):
        print ("Welcome to Python! %s Programming Language!" % self.version)

hello = HelloWorld()
hello.welcome()

