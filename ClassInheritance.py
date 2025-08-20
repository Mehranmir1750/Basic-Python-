class Parent:
    def show(self):
        print("Parent Class")

class Child(Parent):

    def show(self):
        super().show()
        print("Child class")

c = Child()
c.show() 
