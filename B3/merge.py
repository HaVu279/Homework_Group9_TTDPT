from PIL import Image

red = Image.open('red_image.jpg')
green = Image.open('green_image.jpg')
blue = Image.open('blue_image.jpg')

img = Image.merge("RGB", (red, green, blue))

img.save('image.jpg')
img.show()