class parent:
    def __init__(self):
        print("Parent Constructor")

    def displayDetails(self):
        print("Parent Display Details")

class child(parent):
    def __init__(self):
        print("Child construct")

    def  displayChildDetails(self):
        print("Child display details")


obj = child()

print(obj)

obj.displayChildDetails()
obj.displayDetails()