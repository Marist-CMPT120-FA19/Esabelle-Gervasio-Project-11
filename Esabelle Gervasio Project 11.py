#Esabelle Gervasio
#Project 11
from math import *

class Sphere:

    def __init__(self, radius):
        self.radius= radius
        self.volume = ((4/3)*pi*(self.radius**3))
        self.surfacearea = (4*pi*(self.radius**2))

    def Radius (self):
        return self.radius

    def Surfacearea(self):
        return self.surfacearea

    def Volume(self):
        return self.volume
    
def main():
    
    radius= float(input("Enter a number for the radius: "))
    oneSphere= Sphere(radius)
    print("The volume of this sphere is: ", oneSphere.Volume())
    print("The surface area of this sphere is: ", oneSphere.Surfacearea())

if __name__ == '__main__':
    main()
