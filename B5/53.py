import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

fig, ax = plt.subplots(figsize=(6, 6))
l=500

for x in range(l*6):
    if x < l :
        c1='red' 
        c2='orange' 
        ax.axhline(x, color=colorFader(c1,c2,x/l), linewidth=0.5)
    if l < x < l*2:
        c1='orange' 
        c2='yellow' 
        ax.axhline(x, color=colorFader(c1,c2,(x-l)/l), linewidth=0.5)
    if 2*l < x < 3*l:
        c1='yellow' 
        c2='green' 
        ax.axhline(x, color=colorFader(c1,c2,(x-2*l)/l), linewidth=0.5)
    if 3*l < x < 4*l:
        c1='green' 
        c2='blue'
        ax.axhline(x, color=colorFader(c1,c2,(x-3*l)/l), linewidth=0.5)
    if 4*l < x < 5*l:
        c1='blue' 
        c2='indigo' 
        ax.axhline(x, color=colorFader(c1,c2,(x-4*l)/l), linewidth=0.5)
    if 5*l < x < 6*l:
        c1='indigo' 
        c2='violet'
        ax.axhline(x, color=colorFader(c1,c2,(x-5*l)/l), linewidth=0.5)
plt.show()
