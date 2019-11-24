from PIL import Image

img = Image.open('2.png')

rgb = Image.Image.split(img)

rgb[0].save('red_image.png')
rgb[1].save('green_image.png')
rgb[2].save('blue_image.png')

if(img.mode == 'RGBA'):
    rgb[3].save('anpha_image.png')
