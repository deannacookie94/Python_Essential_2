import math

"""
Objectives
improving the student's skills in defining classes from scratch;
using composition.

Scenario
Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?

The new class will be called Triangle and this is the list of our expectations:

the constructor accepts three arguments - all of them are objects of the Point class;
the points are stored inside the object as a private list;
the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is a sum of all legs' lengths (we mention it for the record, although we are sure that you know it perfectly yourself.)
Complete the template we've provided in the editor. Run your code and check whether the evaluated perimeter is the same as ours.

Copy the Point class code we used in the previous lab:

Expected output
3.414213562373095

"""

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return math.hypot(abs(self.__x - point.getx()), abs(self.__y - point.gety()))

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
       self.__verticesList = [vertice1, vertice2, vertice3]

    def perimeter(self):
        self.__perimeter = self.__verticesList[0].distance_from_xy(self.__verticesList[1].getx(),self.__verticesList[
            1].gety()) + self.__verticesList[1].distance_from_xy(self.__verticesList[2].getx(),self.__verticesList[
            2].gety()) + self.__verticesList[2].distance_from_xy(self.__verticesList[0].getx(),self.__verticesList[
            0].gety())
            #.distance_from_point(self.__verticesList[1])

        return self.__perimeter
        #str(self.__v1v2distance + self.__v2v3distance + self.__v3v1distance)

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
