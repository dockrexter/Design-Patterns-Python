class car:
    def __init__(self):
        print ("car production started")

class jeep:
    def __init__(self):
        print ("jeep production started")

class toyFactory(car,jeep):
    def __init__(self,type):
        if(type=="jeep"):
            jeep()
        else:
            car()

produce=toyFactory("car")
produce=toyFactory("jeep")

