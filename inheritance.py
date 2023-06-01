class Polygon:
    # Initializing the number of sides
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]


    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]


    # method to display the length of each side of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Triangle(Polygon):
    # Initializing the number of sides of the triangle to 3 by 
    # calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self,3)


    def findArea(self):
        a, b, c = self.sides


        # calculate the semi-perimeter
        s = (a + b + c) / 2


        # Using Heron's formula to calculate the area of the triangle
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)


# Creating an instance of the Triangle class
t = Triangle()


# Prompting the user to enter the sides of the triangle
t.inputSides()


# Displaying the sides of the triangle
t.dispSides()


# Calculating and printing the area of the triangle
t.findArea()
