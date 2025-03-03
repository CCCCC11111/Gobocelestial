import csv
import math as m
Mf=[]

with open('CIE.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        Mf.append(lines)
  file.close()
TXT=[]

def M(x,T):
    c=299792458
    h=6.62607015*10**-34
    k=1.380649*10**-23
    c2=h*c/k
    return (1/((x**5)*(m.exp(c2/(x*T))-1)))


def TemptoRGB(T):
    X =0
    Y=0
    Z=0
    for i in Mf:
        X+=float(i[1])*M(float(i[0])/1000000000,T)
        Y+=float(i[2])*M(float(i[0])/1000000000,T)
        Z+=float(i[3])*M(float(i[0])/1000000000,T)
    x=(X*2.55)/(X+Y+Z)
    y=(2.55*Y)/(X+Y+Z)
    z=(2.55*Z)/(Z+Y+Z)


    Matrix= [[3.2404542,-1.5371385,-0.4985314],
            [-0.9692600,1.8780108,0.0415560],
            [0.0556434,-0.2040259,1.0572252]]
    R = Matrix[0][0]*x+ Matrix[0][1]*y+ Matrix[0][2]*z
    G = Matrix[1][0]*x+ Matrix[1][1]*y+ Matrix[1][2]*z
    B = Matrix[2][0]*x+ Matrix[2][1]*y+ Matrix[2][2]*z
    if(R >0.0031308):
        R=1.055*(R**(1/2.4))-0.055
    else:
        R=12.92*R
    if(G >0.0031308):
        G=1.055*(G**(1/2.4))-0.055
    else:
        G=12.92*G
    if(B >0.0031308):
        B=1.055*(B**(1/2.4))-0.055
    else:
        B=12.92*B
    
    if(R>1):
        B=B/R
        G=G/R
        R=1
    

    return(255*R,255*G,255*B)



with open('temperatures.txt', mode ='r')as file:
    for line in file:
        Temp= int(line.split()[1])
        RGB= TemptoRGB(Temp)
        l = line.split()
        l.append(str(round(RGB[0])))
        l.append(str(round(RGB[1])))
        l.append(str(round(RGB[2])))
        TXT.append(" ".join(l))
        print(l)
    file.close()

f = open("temperatures.txt", "w")
for i in TXT:
    f.write(i)
    f.write("\n")
f.close()
      


