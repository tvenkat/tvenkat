class ReverseString:
    """
    reverse a string
    """

    def __init__(self, string_input):

        self.string_input = string_input
        self.string_out = ''
        self.length = len(string_input) - 1

    def reverse_string(self):
        """
        reverse a give string, print and check if its palindrome or not
        """

        print "Given String %s and Its length %d" % (self.string_input, self.length)
        while self.length >=0:
            self.string_out = self.string_out + self.string_input[self.length]
            self.length -= 1
        print 'Reversed String', self.string_out
        if self.string_out == self.string_input:
            print 'Yes its a palindrome'
        else:
            print 'Nope its not Palindrome'
        print '#' * 30

Reverse = ReverseString('malayalam')
Reverse.reverse_string()

Reverse = ReverseString('tvenkat')
Reverse.reverse_string()