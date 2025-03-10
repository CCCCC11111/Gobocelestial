import math as m
from Temperaturetocolor import *
scalex = 8.64*m.pi
scaley = 8.64*m.pi
n=3
Center = n*m.pi/6

def to_gallpeter(a,d):
    x=scalex*(a-m.pi)
    y=scaley*m.sin(d)
    return (x,y)
def to_cassini(a,d):
    x=scalex*m.asin(m.cos(d)*m.sin(a-Center))
    y=scaley*m.atan2(m.tan(d),m.cos(a-Center))
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
    def getPos(self):
        return to_cassini(self.asc,self.dec)
    def getColor(self,Array):
        Sp=str(self.spec[0])[2]+str(self.spec[1])[2]
        return TemptoRGB(Sp,Array)
    