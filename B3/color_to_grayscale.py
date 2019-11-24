from PIL import Image

img = Image.open('1.png').convert('L')
img.show()
img.save('grayscale.png')