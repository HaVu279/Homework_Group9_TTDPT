import winsound

def win_wav_play(filename):
    winsound.PlaySound(filename, winsound.SND_LOOP)

def numbers_to_strings(argument): 
    switcher = { 
        0: "A3", 
        1: "A3#", 
        2: "B3",
        3: "C3", 
        4: "C3#", 
        5: "C4",
        6: "D3", 
        7: "D3#", 
        8: "E3",
        9: "F3", 
        10: "F3#", 
        11: "G3",
        12: "G3#",
    } 
    return switcher.get(argument, "nothing") 

print("Menu file wav")
print("0.A3")
print("1.A3#")
print("2.B3")
print("3.C3")
print("4.C3#")
print("5. C4")     
print("6.D3")
print("7.D3#")
print("8.E3")
print("9.F3")
print("10.F3#")
print("11.F3")
print("12.G3#")
      
print("Enter file wav:", end=" ")
choose = int(input())

filename = numbers_to_strings(choose)
Play = win_wav_play(filename)
