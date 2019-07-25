class services:
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name

class customer:
    def __init__(self,service):
        self.service=service

    def getservice(self):
        print (self.service.getname())



s1=services("carserviice")
s2=services("bikeservice")

c1=customer(s1)
c2=customer(s2)

c1.getservice()
c2.getservice()