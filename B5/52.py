import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

fig, ax = plt.subplots(figsize=(6, 6))

l=500

m=l*6

for x in range(m):
    if x < l :
        c1='red'
        c2='orange'
        ax.axvline(x, color=colorFader(c1,c2,x/l), linewidth=0.5)
    if l < x < (2*l):
        c1='orange'
        c2='yellow'
        ax.axvline(x, color=colorFader(c1,c2,(x-l)/l), linewidth=0.5)
    if 2*l < x < 3*l:
        c1='yellow'
        c2='green'
        ax.axvline(x, color=colorFader(c1,c2,(x-2*l)/l), linewidth=0.5)
    if 3*l < x < 4*l:
        c1='green'
        c2='blue'
        ax.axvline(x, color=colorFader(c1,c2,(x-3*l)/l), linewidth=0.5)
    if 4*l < x < 6*l:
        c1='blue'
        c2='indigo'
        ax.axvline(x, color=colorFader(c1,c2,(x-4*l)/l), linewidth=0.5)
    if 5*l < x < 6*l:
        c1='indigo'
        c2='violet'
        ax.axvline(x, color=colorFader(c1,c2,(x-5*l)/l), linewidth=0.5)

plt.show()
