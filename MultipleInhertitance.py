class A:
    def show(self):
        print("Parent A")

class B:
    def show(self):
        print("Parent B")

class C(A,B):
    def show(self):
        super().show()
        print("Child class")

obj = C()
obj.show()