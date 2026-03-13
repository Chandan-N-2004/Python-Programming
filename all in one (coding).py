# example using property function
class person:
    def __init__(self):
        self.__name="  "
        self.__age=" "
    
    def getter(self):
        return self.__name, self.__age
    
    
    def setter(self, value1, value2):
        self.__name=value1
        self.__age=value2
        print(self.__name)
    
    getset=property(getter, setter)
    
p=person()
p.getset="rama", 21
res,res1=p.getset
print(res)
print(res1)