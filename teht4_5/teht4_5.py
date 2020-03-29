from plotter import Circle, render

def main():
    a = Circle(5, 5, 2)
    b = Circle(-2, 2, 1)
    c = Circle(0, 0, 10) 
    render([a, b, c])

    print('Siirretään b:tä 10 ylöspäin')
    b.move(0, 10)
    print('Siirretään c:tä vasemmalle')
    c.move(-5, 0) 
    render([a, b, c]) 

if __name__ == "__main__":
    main()