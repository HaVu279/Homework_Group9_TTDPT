from PIL import Image

img = Image.open('1.jpg').convert('L')
img.show()
img.save('grayscale.jpg')