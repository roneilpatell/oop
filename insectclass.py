import random 

class Insect:
    def __init__(self,w,l,n):
        self.legs = l
        self.wings = w
        self.name = n
        self.miles = 0
    
    def flightime(self):
        self.miles = random.randint(1,10)

    def getflighttime(self):
        return self.miles
    
    def getname(self):
        return self.name