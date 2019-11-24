from scipy.io.wavfile import write
from numpy import linspace,sin,pi,int16

def note(freq, len, amp=1, rate=20000):
 t = linspace(0,len,len*rate)
 data = sin(2*pi*freq*t)*amp
 return data.astype(int16) # two byte integers

def CreateWav (f, name):
    tone = note(f,2,amp=10000)
    write(name,40000,tone)
    
f=261.63
CreateWav(f, "C3.wav")
f*=(2**(1/12))
CreateWav(f, "C3#.wav")
f*=(2**(1/12))
CreateWav(f, "D3.wav")
f*=(2**(1/12))
CreateWav(f, "D3#.wav")
f*=(2**(1/12))
CreateWav(f, "E3.wav")
f*=(2**(1/12))
CreateWav(f, "F3.wav")
f*=(2**(1/12))
CreateWav(f, "F3#.wav")
f*=(2**(1/12))
CreateWav(f, "G3.wav")
f*=(2**(1/12))
CreateWav(f, "G3#.wav")
f*=(2**(1/12))
CreateWav(f, "A3.wav")
f*=(2**(1/12))
CreateWav(f, "A3#.wav")
f*=(2**(1/12))
CreateWav(f, "B3.wav")
f*=(2**(1/12))
CreateWav(f, "C4.wav")