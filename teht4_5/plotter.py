import math
import matplotlib.pyplot as plt

def render(shapes):
    ax = plt.gca()
    for shape in shapes:
        ax.add_patch(shape.plottable())
    plt.axis('scaled')
    plt.show()

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

    def plottable(self):
        return plt.Circle((self.x, self.y), radius = self.r, fill=False)

if __name__ == "__main__":
    print('pls, just a module. use different main. see src for usage.')