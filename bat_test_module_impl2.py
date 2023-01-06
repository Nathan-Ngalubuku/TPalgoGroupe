"""
TRAVAIL FAIT PAR LES MEMBRES DU GROUPE 17 : NGALUBUKU, RUKENGEZA, SHUKANYA

"""
from module_impl2 import*
import random

import time as tm
class formegeometrique:       
 
    start=tm.time()

    print("1) CALCUL DU PERIMETRE ET DE LA SURFACE DU RECTANGLE. ")
    print("-----------------------------------------------------")
    a=float(random.randint(1,50))
    b=float(random.randint(1,50))

    rect=rectangle(a,b)
    print(" - LA SURFACE DU RECTANGLE EST : ",rect.surface())
    print(" - LE PERIMETRE DU RECTANGLE EST : ",rect.perimetre())
    print("")
    

    print("2) CALCUL DU PERIMETRE ET DE LA SURFACE DU TRIANGLE. ")
    print("----------------------------------------------------")
    a=float(random.randint(1,50))
    b=float(random.randint(1,50))
    c=float(random.randint(1,50))
    d=float(random.randint(1,50))
    tri=triangle(a,b,c,d)
    print(" - LA SURFACE DU TRIANGLE EST :  ",tri.surface())
    print(" - LE PERIMETRE DU TRIANGLE EST : ",tri.perimetre())
    print("")

    
    print("3) CALCUL DE LA CIRCONFERENCE ET DE LA SURFACE DU CERCLE. ")
    print("---------------------------------------------------------")  
    a=float(random.randint(1,50))
     
    
    cer=cercle(a)
    print(" - LA SURFACE DU CERCLE EST  : ",cer.surface())
    print(" - LA CIRCONFERENCE DU CERCLE EST : ",cer.perimetre())
    print("")
     
        
        
    
    print("4) CALCUL DE LA SURFACE ET DU PERIMETRE DU CARRE. ")
    print("-------------------------------------------------")
    a=float(random.randint(1,50))
        
        
    car=carre(a)
    print(" - LA SURFACE DU CARREE EST  :  ",car.surface())
    print(" - LE PERIMETRE DU CARRE EST : ",car.perimetre())
    print("")
    
    print("5) CALCUL DU PERIMETRE ET DE LA SURFACE DU TRIANGLE RECTANGLE. ")
    print("--------------------------------------------------------------")
    a=float(random.randint(1,50))
    b=float(random.randint(1,50))
    c=float(random.randint(1,50))
        
    
    tri=triangleRectangle(a,b,c)
    print(" - LA SURFACE DU TRIANGLE RECTANGLE EST :  ",tri.surface())
    print(" - LE PERIMETRE DU TRIANGLE RECTANGLE EST : ",tri.perimetre())
    print("")    
    
    end=tm.time()
    
    temps= end-start
    
    
    print(" LE TEMPS D'EXECUTION EST : ", temps)
        
        
        