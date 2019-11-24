import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return (1-mix)*c1 + mix*c2


l=200
m = l*3
Figure = np.zeros((m, m, 3))

for x in range(m):
    for y in range(x+1):
        if x < l :
            c1='red'
            c2='orange'
            Figure[x-y][y] = colorFader(c1,c2,x/l)
        if (l) <= x < (2*l):
            c1='orange'
            c2='yellow'
            Figure[x-y][y] = colorFader(c1,c2,(x-l)/l)
        if (2*l) <= x < (3*l):
            c1='yellow' 
            c2='green' 
            Figure[x-y][y] = colorFader(c1,c2,(x-2*l)/l)
            
for x in range(m-1):
    for y in range(x+1):
        if (2*l) <= x < (3*l-1):
            c1='blue' 
            c2='green' 
            Figure[m-1-y][m-1+y-x] = colorFader(c1,c2,(x-2*l)/l)
        if (l) <= x < (2*l):
            c1='indigo' 
            c2='blue' 
            Figure[m-1-y][m-1+y-x] = colorFader(c1,c2,(x-l)/l)
        if  x < (l):
            c1='violet' 
            c2='indigo' 
            Figure[m-1-y][m-1+y-x] = colorFader(c1,c2,(x)/l)
            
plt.subplots(figsize=(6, 6))
plt.imshow(Figure)
plt.show()
