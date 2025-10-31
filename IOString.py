class string:

    def __init__(self):
        self.str1 = ''
    
    def inputation(self):
        self.str1 = input("Enter a string or word")
    
    def upper_user(self):
        print("The upper case of this word is", self.str1.upper())

obj = string()
obj.inputation()
obj.upper_user()
    