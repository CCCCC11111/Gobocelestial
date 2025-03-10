

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
         k=float(constPoints[i][0]),float(constPoints[i][1])
         j=float(constPoints[i+1][0]),float(constPoints[i+1][1])
         lines.append([(k[0],k[1],0),(j[0],j[1],0)])

for l in lines:
    if l[0][0]== l[1][0]:
        for L in lines:
            if l!=L and l[0][0]==L[0][0]:
                upl=
                upL=
                down
                if(L[0][1]>l[0][1]):
                    


         
    
          