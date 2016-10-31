import math

class Triangulo:
    
    def __init__(self,lado_A,lado_B,lado_C):
        self.__lado_A=lado_A
        self.__lado_B=lado_B
        self.__lado_C=lado_C
        self.__perimetro=self.calPerimetro()
        self.__area=0
        
    def getLadoA(self):
        return self.__lado_A
    
    def getLadoB(self):
        return self.__lado_B
    
    def getLadoC(self):
        return self.__lado_C
    
    def getPerimetro(self):
        return self.__perimetro
    
    def getArea(self):
        return self.__area
    
    def setPerimetro(self, perimetro):
        self.__perimetro=perimetro
        
    def setArea(self):
        self.__area=self.calArea()
    
    def isTriangulo(self):
        if self.getLadoA()+self.getLadoB()>self.getLadoC():
            if self.getLadoB()+self.getLadoC()>self.getLadoA():
                if self.getLadoA()+self.getLadoC()>self.getLadoB():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def calPerimetro(self):
        perimetro=self.getLadoA()+self.getLadoB()+self.getLadoC()
        return perimetro
        
    def calAngulo(self):
        a=self.getLadoA()
        b=self.getLadoB()
        c=self.getLadoC()
        cosa= (a**2+b**2-c**2)%(2*a*b)
        angulo=math.acos(cosa)
        return angulo
    
    def calArea(self):
        angulo=self.calAngulo()
        base=self.getLadoA()*math.sin(angulo)
        altura=self.getLadoB()*math.cos(angulo)
        area=(base*altura)/2
        return area
    

tri=Triangulo(3,4,5)
print(tri.getPerimetro())
print(tri.calArea())