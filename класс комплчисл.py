class Complex():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __abs__(self):
        return (self.x**2 +self.y**2)**0.5
    def __add__(self, other):
        z=Complex()
        z.x=self.x +other.x
        z.y=self.y +other.y
        return z
    def __sub__(self, other):
        z=Complex()
        z.x=self.x - other.x
        z.y=self.y - other.y
        return z
    def __mul__(self, other):
        z=Complex()
        z.x=self.x * other.x - self.y * other.y
        z.y=self.x * other.y + self.y * other.x
        return z
    def __div__(self, other):
        z = self
        R = Complex(other.x, -other.y)
        z = z * R 
        z.x = z.x / abs(R)
        z.y = z.y / abs(R)
        return z
    

    






    

































