""" TRAVAIL FAIT PAR LES MEMBRES DU GROUPE 17 : NGALUBUKU, RUKENGEZA, SHUKANYA
"""
import math

class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
        
    def surface(self):
        return self.height*self.width
    
    def perimeter(self):

        return (self.height+self.width)*2

class Circle:
    def __init__(self,radius):
        self.radius=radius
        
        
    def surface(self):
        return math.pi*self.radius**2
        
    def perimeter(self):
        return 2*math.pi*self.radius

class Triangle:
    def __init__(self,height,c1,c2,c3):
        self.height=height
        self.c1=c1
        self.c2=c2
        self.c3=c3

    def surface(self):
        return self.height*self.c1/2
    
    def perimeter(self):
        return (self.c1+self.c2+self.c3)
class Square:
    def __init__(self,side):
        self.side=side
        
        
    def surface(self):
        return self.side**2
    
    def perimeter(self):
        return self.side*4
    
    

class TriangleRectangle:
    def __init__(self,height,c1,hypotenus):
        self.height=height
        self.c1=c1
        self.hypotenus=hypotenus
        

    def surface(self):
        return self.height*self.c1/2
    
    def perimeter(self):
        return (self.c1+self.height+self.hypotenus)
