# Iteration Sample with StopIteration #
class MyNumbers:
    def __init__(self,startVal, stopVal):
        self.a = startVal
        self.stop = stopVal

    def __iter__(self):
        return self

    def __next__(self):
        if(self.a <= self.stop):
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

start = 15
stop = 30
obj = MyNumbers(start,stop)
myiter = iter(obj)

""" Loop thorugh Iteration """
for x in myiter:
  print(x)
