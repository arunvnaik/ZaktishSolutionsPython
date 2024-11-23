class Solution:
    def __init__(self, name,age):
        self.name=name 
        self.age=age 
        
    def printname(self):
        print(self.name) 
        
class Newclass(Solution): 
    pass 
        
solution=Newclass('harish',61)

solution.printname() 
