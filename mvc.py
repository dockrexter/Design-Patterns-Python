class model:
    def __init__(self,name):
        self.name=name
    def returning(self,message):
        if message == "name":
            return self.name
        else:
            return "required information not available" 

class view:
    def __init__(self,message):
        print (message)

class controller(model,view):
    def __init__(self,request):
        information=model("ghost").returning(request)
        view(information)


controller("name")
