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
         k=(float(constPoints[i][0]),float(constPoints[i][1]))
         j=(float(constPoints[i+1][0]),float(constPoints[i+1][1]))
         for i in range(9):
            dx=(j[0]-k[0])/10
            dy=(j[1]-k[1])/10
            lines.append([((k[0]+dx*i)*DEGREES,(k[1]+dy*i)*DEGREES,0),((k[0]+dx*(i+1))*DEGREES,(k[1]+dy*(i+1))*DEGREES,0)])


         
    
          
            
        
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

          

config.pixel_height = 1920
config.pixel_width = 320

meridians = []
parallels = []
for i in range(-1,2):
    M=[]
    for j in range(-90,91):
         C=(i*15*DEGREES+Center,j*DEGREES)
         M.append(to_cassini(C[0],C[1]))
    meridians.append(M)

for i in range(-90,91,10):
    P=[]
    for j in range(-15,16):
         C=(j*DEGREES+Center,i*DEGREES)
         P.append(to_cassini(C[0],C[1]))
    parallels.append(P)

def to_cassini3D(P):
    x=scalex*m.asin(m.cos(P[1])*m.sin(P[0]-Center))
    y=scaley*m.atan2(m.tan(P[1]),m.cos(P[0]-Center))
    return (x,y,0)

def ecliptic(x):
    return (m.atan2(m.cos(23.44*DEGREES)*m.sin(x),m.cos(x)),m.asin(m.sin(x)*m.sin(23.44*DEGREES)))
ecliptic_points=[]
print("Ecliptic")
for x in range(361):
    
    print(to_cassini3D(ecliptic(x*DEGREES)))
    ecliptic_points.append(to_cassini3D(ecliptic(x*DEGREES)))
    
def prececionN(x):
    return (m.atan2(m.sin(2*23.44*DEGREES)/2*(m.sin(x)-1),m.cos(x)*m.sin(23.44*DEGREES)),m.asin(m.sin(x)*m.sin(23.44*DEGREES)**2+m.cos(23.44*DEGREES)**2))
def prececionS(x):
    return (m.atan2(m.sin(2*23.44*DEGREES)/2*(m.sin(x)+1),m.cos(x)*m.sin(23.44*DEGREES)),m.asin(m.sin(x)*m.sin(23.44*DEGREES)**2-m.cos(23.44*DEGREES)**2))
prececion_pointsN=[]
prececion_pointsS=[]
for x in range(181):
    prececion_pointsN.append(to_cassini3D(prececionN(2*x*DEGREES)))
    prececion_pointsS.append(to_cassini3D(prececionS(2*x*DEGREES)))

     


class MAKEMAP(Scene):
    def construct(self):

        for i in meridians:
            for j in range(len(i)-1):
                 l = Line((i[j][0],i[j][1],0),(i[j+1][0],i[j+1][1],0), color="#FFFFFF")
                 l.set_stroke(width=1)
                 self.add(l)

        for i in parallels:
            for j in range(len(i)-1):
                 l = Line((i[j][0],i[j][1],0),(i[j+1][0],i[j+1][1],0), color="#FFFFFF")
                 l.set_stroke(width=1)
                 self.add(l)
        
        for L in lines:
            Q=to_cassini3D(L[0])
            P=to_cassini3D(L[1])
            if((Q[0]<PI/12*scalex and Q[0]>-PI/12*scalex and Q[1]<PI/2*scaley and Q[1]>-PI/2*scaley) or (P[0]<PI/12*scalex and P[0]>-PI/12*scalex and P[1]<PI/2*scaley and P[1]>-PI/2*scaley)):
                l= DashedLine(Q,P,dash_length=0.05, dashed_ratio=0.3)
                l.set_stroke(width=2)
                self.add(l)

        for i in range(len(ecliptic_points)-1):
            if((ecliptic_points[i][0]<PI/12*scalex and ecliptic_points[i][0]>-PI/12*scalex and ecliptic_points[i][1]<PI/2*scaley and ecliptic_points[i][1]>-PI/2*scaley) or (ecliptic_points[i+1][0]<PI/12*scalex and ecliptic_points[i+1][0]>-PI/12*scalex and ecliptic_points[i+1][1]<PI/2*scaley and ecliptic_points[i+1][1]>-PI/2*scaley)):
                l= Line(ecliptic_points[i],ecliptic_points[i+1],color=RED)
                l.set_stroke(width=5)
                self.add(l)
                if i%10==0:
                    a=m.atan2((ecliptic_points[i+1][1]-ecliptic_points[i][1]),(ecliptic_points[i+1][0]-ecliptic_points[i][0]))-PI/2
                    P=(ecliptic_points[i][0]+0.4*m.cos(a),ecliptic_points[i][1]+0.4*m.sin(a),0)
                    Q=(ecliptic_points[i][0]-0.4*m.cos(a),ecliptic_points[i][1]-0.4*m.sin(a),0)
                    l = Line(P,Q,color=RED)
                    l.set_stroke(width=5)
                    self.add(l)

        for i in range(len(prececion_pointsN)-1):
            if((prececion_pointsN[i][0]<PI/12*scalex and prececion_pointsN[i][0]>-PI/12*scalex and prececion_pointsN[i][1]<PI/2*scaley and prececion_pointsN[i][1]>-PI/2*scaley) or (prececion_pointsN[i+1][0]<PI/12*scalex and prececion_pointsN[i+1][0]>-PI/12*scalex and prececion_pointsN[i+1][1]<PI/2*scaley and prececion_pointsN[i+1][1]>-PI/2*scaley)):
                l= Line(prececion_pointsN[i],prececion_pointsN[i+1],color=BLUE)
                l.set_stroke(width=4)
                self.add(l)
        for i in range(len(prececion_pointsS)-1):
            if((prececion_pointsS[i][0]<PI/12*scalex and prececion_pointsS[i][0]>-PI/12*scalex and prececion_pointsS[i][1]<PI/2*scaley and prececion_pointsS[i][1]>-PI/2*scaley) or (prececion_pointsS[i+1][0]<PI/12*scalex and prececion_pointsS[i+1][0]>-PI/12*scalex and prececion_pointsS[i+1][1]<PI/2*scaley and prececion_pointsS[i+1][1]>-PI/2*scaley)):
                l= Line(prececion_pointsS[i],prececion_pointsS[i+1],color=BLUE)
                l.set_stroke(width=4)
                self.add(l)


        for mp in Month_pos:
            month=Circle(0.3,color=RED)
            C=to_cassini3D(ecliptic(mp*DEGREES))
            month.set_x(C[0])  
            month.set_y(C[1])
            self.add(month)
                    

                
        ''' 
        eclip_angle=23.44
        axes = Axes(
        x_range = (-PI*scalex, PI*scalex),
        y_range = (-scaley, scaley),
        y_length=2*scaley,
        x_length=2*PI*scalex,
        axis_config={"include_numbers": False},)
        
             
        def f(x):
            if x <= -PI/2*scalex: return scaley*m.sin(m.atan(m.tan((x/scalex))/m.cos(eclip_angle*DEGREES)))*m.sin(eclip_angle*DEGREES)
            if x <= PI/2*scalex: return -scaley*m.sin(m.atan(m.tan((x/scalex))/m.cos(eclip_angle*DEGREES)))*m.sin(eclip_angle*DEGREES)
            return scaley*m.sin(m.atan(m.tan((x/scalex))/m.cos(eclip_angle*DEGREES)))*m.sin(eclip_angle*DEGREES)
            
        
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
        '''


        for s in Stars: 
            if(s.getPos()[0]< PI/12*scalex and s.getPos()[0]>-PI/12*scalex and s.getPos()[1]<scaley*PI/2 and s.getPos()[1]>-scaley*PI/2):
                size= 0.3/(1.5**(s.mag/100))
                star = Circle(size)
                star.set_stroke(WHITE,0)
            
                star.set_fill(rgb_to_color(s.getColor(Array)),opacity=1)
                star.set_x(s.getPos()[0])
                star.set_y(s.getPos()[1])
                self.add(star)  # show the circle on screen
