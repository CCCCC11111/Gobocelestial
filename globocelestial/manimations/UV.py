from manim import *
from Star import *
import struct
Stars = []
Array =[]

with open('temperatures.txt', mode ='r')as file:
    for line in file:
        lin = line.split()[0]
        l=[]
        l.append(lin)
        l.append(int(line.split()[5]))
        l.append(int(line.split()[6]))
        l.append(int(line.split()[7]))
        Array.append(l)
constPoints=[]
with open('ConstelationsE1875.txt', mode ='r')as file:
    for line in file:
        if line[0]=="#":
             constPoints.append([])
        else:
            constPoints.append(line.split())
lines =[]
for i in range(len(constPoints)-1):
    if constPoints[i]!=[] and constPoints[i+1]!=[]:
         k=to_gallpeter(float(constPoints[i][0])*DEGREES,float(constPoints[i][1])*DEGREES)
         j=to_gallpeter(float(constPoints[i+1][0])*DEGREES,float(constPoints[i+1][1])*DEGREES)
         lines.append([(k[0],k[1],0),(j[0],j[1],0)])

         
    
          
            
        
with open("PPM", "rb") as f:
        header_data = f.read(28)
        # Read the 28-byte header
        header_format = ">7i"
        unpacked= struct.unpack(header_format,header_data)
        #print(unpacked)
        for i in range(378910):
                star_data= f.read(28)
                magnitude= struct.unpack(">h",star_data[18:20])[0]
                if magnitude<=600:
                    ascension= struct.unpack(">d",star_data[0:8])[0]
                    #print("Ascension: ",ascension)
                    declination= struct.unpack(">d",star_data[8:16])[0]
                    #print("Declination ",declination)
                    spectral_type= struct.unpack(">2c",star_data[16:18])
                    #print("Spectral Type: ", spectral_type[0], spectral_type[1])
                    #print("Magnitude: ",magnitude)
                    ascensionMotion= struct.unpack(">f",star_data[20:24])[0]
                    declinationMotion= struct.unpack(">f",star_data[24:28])[0]
                    Stars.append(Star(ascension,declination,spectral_type,magnitude,ascensionMotion,declinationMotion))
Month_pos=[]
with open("Months", "r") as f:
     for line in f:
          Month_pos.append(float(line.split()[1]))
          

class MAKEMAP(Scene):
    def construct(self):
        eclip_angle=23.44
        axes = Axes(
        x_range = (-PI*scalex, PI*scalex),
        y_range = (-scaley, scaley),
        y_length=2*scaley,
        x_length=2*PI*scalex,
        axis_config={"include_numbers": False},)
        for L in lines:
             l= DashedLine(L[0],L[1],dash_length=0.05, dashed_ratio=0.5)
             l.set_stroke(width=0.1)
             self.add(l)
        def f(x):
            if x <= -PI/2*scalex: return scaley*m.sin(m.atan(m.tan((x/scalex))/m.cos(eclip_angle*DEGREES)))*m.sin(eclip_angle*DEGREES)
            if x <= PI/2*scalex: return -scaley*m.sin(m.atan(m.tan((x/scalex))/m.cos(eclip_angle*DEGREES)))*m.sin(eclip_angle*DEGREES)
            return scaley*m.sin(m.atan(m.tan((x/scalex))/m.cos(eclip_angle*DEGREES)))*m.sin(eclip_angle*DEGREES)
              
        for mp in Month_pos:
            month=Circle(0.03,color=RED)
            month.set_x(scalex*(mp-PI))
            month.set_y(f(scalex*(mp-PI)))
            self.add(month)
        for i in range(1,24):
            l = Line((scalex*(i*15*DEGREES-PI),-scaley,0),(scalex*(i*15*DEGREES-PI),scaley,0), color="#2B3F69")
            l.set_stroke(width=0.2)
            self.add(l)
        for i in range(-8,9):
            l = Line((-PI*scalex,scaley*m.sin(10*DEGREES*i),0),(PI*scalex,scaley*m.sin(10*DEGREES*i),0),color="#2B3F69")
            l.set_stroke(width=0.2)
            self.add(l)
        ecliptic = axes.plot(f, color = RED)
        ecliptic.discontinuities=[PI/2]
        equator= Line((-PI*scalex,0,0),(PI*scalex,0,0))
        ecliptic.set_stroke(width=0.3)
        equator.set_stroke(width=0.1)
        self.add(ecliptic)
        self.add(equator)

        for s in Stars:
            size= 0.04/(1.58489319246**(s.mag/100))
            star = Circle(size)
            star.set_stroke(WHITE,0)
            
            star.set_fill(rgb_to_color(s.getColor(Array)),opacity=1)
            star.set_x(s.getGallpeter()[0])
            star.set_y(s.getGallpeter()[1])
            self.add(star)  # show the circle on screen
