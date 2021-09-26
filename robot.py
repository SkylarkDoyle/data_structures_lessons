#Note----    O(1) + O(1) = O(1),          O(1) + O(n) = O(n),      O(1) + O(n^2) = O(n^2)

#Time Complexity -> O(1) 
class Robot:
    def  __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w

    def introduceSelf(self):
        print("My name is " + self.name + ", I am Robot " + self.color + " ,Umm i weigh ") #T= O(1)

#Time Complexity ->  O(1) 
class Person:
    def __init__(self, n, a, o, r ):
        self.name = n
        self.age = a
        self.online = o
        
    def owned(self):
        print("My name is " + self.name + " I am " + self.age + " years old ") #T= O(1)

    
        
