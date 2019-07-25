class singleton():
    _instance=None
    def __new__(self):
        if not self._instance:
            self._instance=super(singleton,self).__new__(self)
            self.y=10
        return self._instance


x=singleton()
print(x.y)
x.y=20

z=singleton()
print(z.y)