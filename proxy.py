class player:
    def __init__(self,name):
        self.name=name
        self.team="Pakistan"
        self.salary="100000"

class manager:
    def __init__(self,player):
        self.managed_player=player
    
    def get(self,request):
        if request=="name":
            print(self.managed_player.name)
        elif request=="team":
            print(self.managed_player.team)
        else:
            print("this information can't be shared")


p=player("haris")
m=manager(p)
m.get("name")
m.get("team")
m.get("salary")