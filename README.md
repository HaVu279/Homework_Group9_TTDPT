# Homework_Group9_TTDPT
# Member group 9
	* Nguyễn Thị Hoài B6
	* Ngô Thị Hiền B3
	* Nguyễn Thị Thu Hà B1
	* Hà Ngọc Linh B2
	* Nguyễn Đăng Huy B5
	* Hoàng Thái Hà B4
Problem 1:

Problem 2:

Problem 3:
1. Convert to grayscale
- B1: open file image
- B2: convert to grayscale with function Image.convert('L')
- B3: Save file image with file name is color_to_grayscale.jpg

2. Split to three file of three channels is R, G, B (not found channel A)
- B1: Open file image
- B2: Split image with function Image.Image.split()
- B3: Save file image with file name: red_image.jpg, green_image.jpg, blue_image.jpg

3. Merge from three file of three channels is R, G, B to the original image
- B1: Open three file image of three channels R, G, B
- B2: Merge image with function Image.merge()
- B3: Save file image with file name: image.jpg
Problem 4:

Problem 5:

Problem 6:
1. Linear-convolution
- B1: Run file linear.py
- B2: Input data of vecto x (ex: 1 0 0 1 8 2)
- B3: Input data of vecto y (ex: 1 0 1)
- B4: Result of linear-convolution: [1, 0, 1, 1, 8, 3, 8, 2]
- B5: Compare result by method convolve() in python
	*Solution 1:
	+ import numpy as np
	+ Call function: np.convolve(x, y)
	+ Compare result
	*Solution 2:
	+ from scipy import signal
	+ Call function: signal.convolve(x, y)
	+ Compare result

2. Cyclic-convolution
- B1: Run file cyclic.py
- B2: Input data of vecto x (ex: 1 0 0 1 8 2)
- B3: Input data of vecto y (ex: 1 0 1)
- B4: Input period (ex: 3)
- B5: Result of cyclic-convolution: [10, 10, 4]

3. Convert linear-convolution to cyclic-convolution
- B1: Run file linear.py
- B2: Input data of vecto x (ex: 1 0 0 1 8 2)
- B3: Input data of vecto y (ex: 1 0 1)
- B4: Result of linear-convolution: [1, 0, 1, 1, 8, 3, 8, 2]
- B5: Input period (ex: 3)
- B6: Result of cyclic-convolution: [10, 10, 4]
