from tkinter import *
from listaOO_01 import Televisor

class Application:
    self.televisor=Televisor()
    
    def __init__(self, master=None):
        self.widget1= Frame(master)
        self.widget1.pack()
        self.controle= Label(self.widget1, text='Controle')
        self.controle.pack()
        
        self.widget2= Frame(master)
        self.widget2['pady']=10
        self.widget2['width']=30
        self.widget2.pack(side=LEFT)
        
        self.widget3= Frame(master)
        self.widget3['pady']=10
        self.widget3['width']=30
        self.widget3.pack(side=RIGHT)
        
        self.canal= Label(self.widget2, text='Canal')
        self.canal.pack(side=LEFT)
        
        self.numeroCanal= Entry(self.widget2)
        self.numeroCanal['width']=20
        self.numeroCanal.pack(side=LEFT)
        
        self.submit= Button(self.widget2)
        self.submit['text']='Mudar Canal'
        self.submit['width']=20
        
        self.aumentarVol= Button(self.widget3)
        self.aumentarVol['text']='Vol +'
        self.aumentarVol.pack()
        
        self.diminuirVol= Button(self.widget3)
        self.diminuirVol['text']='Vol -'
        self.diminuirVol.pack()

    def mudarCanal(self):
        canal=int(self.numeroCanal.get())
        if self.televisor.mudarCanal(canal):
            
    
root=Tk()
Application(root)
root.mainloop()