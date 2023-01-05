# -*- coding: utf-8 -*-
from notreTP import Rectangle, Circle, Triangle, Square, TriangleRectangle, Geometrie 
if __name__ == '__main__':
    print(" A PARTIR DES DIFFERENTES CLASSES DES FORMES GEOMETRIQUES :")
    print()
    try:
        rectangle = Rectangle(" Un Rectangle_1 donné dont :", 14, 7)
        cercle = Circle("Un Cercle_1 donné dont :", 14)
        triangle = Triangle("Un Triangle_1 donné dont :", 9, 6, 7)
        carre = Square("Un Carré_1 donné dont :", 6)
        t_rect = TriangleRectangle("Un Triangle Rectangle donné dont :", 5, 7)
        
        rectangle.descript()
        print("")
        cercle.descript()
        print("")
        triangle.descript()
        print("")
        carre.descript()
        print("")
        t_rect.descript()
        print("")
    except Exception:
        print("ERREUR SUR LE PARAMETRE INSERER .")
    
    print()
    print()
    print("A PARTIR DE LA CLASSE DE BASE : ")
    print()
    figA = Geometrie() 
    figB = Geometrie() 
    figC = Geometrie()
    figD = Geometrie()
    figE = Geometrie()
    
    figA.add(Rectangle("Un Rectangle_2 donné dont :", 14, 5))
    figB.add(Circle("Cercle_2 donné dont :", 6))
    figC.add(Triangle("Triangle_2 donné dont :", 11, 6, 7))
    figD.add(Square("Carré_2 donné dont :", 13))
    figE.add(TriangleRectangle("Triangle Rectangle_2 donné dont :", 15, 7))
    
    figA.descript()
    print("")
    figB.descript()
    print("")
    figC.descript()
    print("")
    figD.descript()
    print("")
    figE.descript()
    
    
    try:
        pass

    except Exception:
        print("ERREUR SUR LE PARAMETRE INSERER .")        
        