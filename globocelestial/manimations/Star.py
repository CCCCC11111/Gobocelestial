import math as m
from Temperaturetocolor import *
scalex = 2.25
scaley = 3.976

def to_gallpeter(a,d):
    x=scalex*(a-m.pi)
    y=scaley*m.sin(d)
    return (x,y)




class Star:
    def __init__(self, asc, dec, spec, mag, vela,veld):
        self.asc = asc
        self.dec = dec
        self.mag = mag
        self.spec = spec
        self.vela =vela
        self.veld = veld
    def getpos(self):
       r=m.cos(self.dec)
       x= m.cos(self.asc)*r
       y=m.sin(self.asc)*r
       z=m.sin(self.dec)
       return (self.d*x,self.d*y,self.d*z)
    def getGallpeter(self):
        return to_gallpeter(self.asc,self.dec)
    def getColor(self,Array):
        Sp=str(self.spec[0])[2]+str(self.spec[1])[2]
        return TemptoRGB(Sp,Array)
    