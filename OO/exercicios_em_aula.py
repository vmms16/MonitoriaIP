class Televisor:
    __VOL_MAX=100
    __VOL_MIN=0
    __CANAL_MAX=99
    __CANAL_MIN=1
    
    def __init__(self):
        self.__canal=1
        self.__vol=0
    
    def getCanal(self):
        return self.__canal
    
    def setCanal(self,canal):
        self.__canal=canal
        
    def getVolume(self):
        return self.__vol
    
    def setVolume(self, volume):
        self.__vol=volume
        
    def getVolMax(self):
        return self.__VOL_MAX
    
    def getVolMin(self):
        return self.__VOL_MIN

    def getCanalMax(self):
        return self.__CANAL_MAX
    
    def getCanalMin(self):
        return self.__CANAL_MIN

    def mudarCanal(self, canal):
        if canal<0 or canal>99:
            self.setCanal(1)
        else:
            self.setCanal(canal)
            
    def aumentarVolume(self):
        if self.getVolume()+1>self.getVolMax():
            return self.getVolMax()
        else:
            self.setVolume(self.getVolume()+1)
            
    def diminuirVolume(self):
        if self.getVolume()-1<self.getVolMin():
            return self.getVolMin()
        else:
            self.setVolume(self.getVolume()-1)
    
    def modificarVolume(self,valor):
        if valor<0:
            if self.getVolume()+valor<self.getVolMin():
                return self.getVolMin()
            else:
                self.setVolume(self.getVolume()+valor)
        else:
            if self.getVolume()+valor>self.getVolMax():
                return self.getVolMax()
            else:
                self.setVolume(self.getVolume()+valor)
                
tv=Televisor()
print(tv.getCanal())
print(tv.getVolume())
tv.modificarVolume(57)
tv.modificarVolume(-10)
print(tv.getVolume())