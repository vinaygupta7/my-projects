class Myclass():
    def __init__(self):
        self.__pri=("I'm private")
        self._pro=("I'm protected")
        self.pub=("I'm public")

ob=Myclass()
print ob.pub
print ob._pro
#print ob.__pri