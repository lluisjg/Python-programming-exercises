class simpleClass:
    def __init__(self):
        self.s=""

    def getString(self):
        print("Give me the string")
        self.s=input()

    def printString(self):
        print(self.s.upper())

x=simpleClass()

x.getString()

x.printString()