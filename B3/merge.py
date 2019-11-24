from PIL import Image
from os import path

red = Image.open('red_image.png')
green = Image.open('green_image.png')
blue = Image.open('blue_image.png')

if(path.exists('a.png')):
    anpha = Image.open('anpha_image.png')
    img = Image.merge("RGBA", (red, green, blue, anpha))
else:
    img = Image.merge("RGB", (red, green, blue))

img.save('image.png')