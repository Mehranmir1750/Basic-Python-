class Subtract:

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __sub__(self, other):

        return Subtract(self.x- other.x, self.y-other.y)
    
    def __str__(self):

        return f"({self.x},{self.y})"
    
p1 = Subtract(10,20)
p2 = Subtract(5,18)

p3 = p1-p2
p4 = p2-p1

print(p3)
print(p4)