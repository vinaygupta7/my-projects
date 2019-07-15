class Myclass():
    def __init__(self):
        self.__pri=("I'm private")
        self._pro=("I'm protected")
        self.pub=("I'm public")

    def __privateMethod(self):
        print ("In Private method")

ob=Myclass()

print ob.pub
print ob._pro
#print ob.__pri

print ob._Myclass__pri
ob._Myclass__privateMethod()