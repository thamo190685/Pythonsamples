class Sample:
    __call = 0;
    funCall = 10;

    def count(self):
        self.__call += 1
        self.funCall += 1
        print("call ",self.__call)
        print("FunCall ", self.funCall)


obj = Sample()
obj.count()
obj.count()
#print(obj.__call)
print(obj.funCall)