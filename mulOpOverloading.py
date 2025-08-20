class Multiply:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Multiply(self.x*other.x, self.y * other.y )
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
p1 = Multiply(4,4)
p2 = Multiply(6,5)

p3 = p1*p2
print(p3)
