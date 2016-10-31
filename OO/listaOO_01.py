from tkinter import *


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
        if canal>=self.getCanalMin() and canal<= self.getCanalMax():
            self.setCanal(canal)
            return True
        else:
            return False
            
    def aumentarVolume(self):
        if self.getVolume()<self.getVolMax():
            self.setVolume(self.getVolume()+1)
        else:
            print('Vol=100')
            
    def diminuirVolume(self):
        if self.getVolume()>self.getVolMin():
            self.setVolume(self.getVolume()-1)
        else:
            print('Vol=0')
            
