import math

class Circle:
    def __init__(self, x, y, r):
        super().__init__()
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi * self.r**2
    
    def circumference(self):
        return 2 * math.pi * self.r
    
    def move(self, i, j):
        self.x = self.x + i
        self.y = self.y + j

    def overlaps(self, circle2):
        centerDistance = math.sqrt((self.x - circle2.x)**2 + (self.y - circle2.y)**2)
        return centerDistance < (self.r + circle2.r)

def main():
    a = Circle(5, 5, 2)
    b = Circle(-2, 2, 1)
    c = Circle(0, 0, 10)
    
    print('Ympyrän a ala:', a.area())
    print('Ympyrän b piiri:', b.circumference())
    print('a ja b ovat päällekkäin:', a.overlaps(b))
    print('b ja c ovat päällekkäin:', b.overlaps(c))
    print('Siirretään b:tä 10 ylöspäin')
    b.move(0, 10)
    print('b ja c ovat päällekkäin:', b.overlaps(c))

if __name__ == "__main__":
    main()