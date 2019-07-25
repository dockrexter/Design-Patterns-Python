class observer:
    def __init__(self,name):
        self.name=name
    def update(self,messages):
        print('{} got message {}'.format(self.name,messages))


class observable:
    def __init__(self):
        self.observers=set()
    def register(self,observer):
        self.observers.add(observer)
    def unregister(self,observer):
        self.observers.discard(observer)
    def dispatch(self,message):
        for observer in self.observers:
            observer.update(message)


obs=observable()

cnn=observer("cnn")
bbc=observer("bbc")

obs.register(cnn)
obs.register(bbc)

obs.dispatch("bomb blast at world trade center")