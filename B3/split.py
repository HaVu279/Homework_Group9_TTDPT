from PIL import Image

img = Image.open('1.jpg')

rgb = Image.Image.split(img)

rgb[0].save('red_image.jpg')
rgb[1].save('green_image.jpg')
rgb[2].save('blue_image.jpg')

rgb[0].show()
rgb[1].show()
rgb[2].show()