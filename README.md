# Homework_Group9_TTDPT
# Member group 9
	* Nguyễn Thị Hoài B6
	* Ngô Thị Hiền B3
	* Nguyễn Thị Thu Hà B1
	* Hà Ngọc Linh B2
	* Vũ Đăng Huy B4
	* Hoàng Thái Hà B5
	
Problem 1:
- B1: Declare variables (A, f, fs, N, n)
- B2: Draw a waveform graph by function plot using pyplot of matplotlib
- B3: Save file image with file name: sin_s1.jpg, sin_s2.jpg
- B4: Run file sinwave.py
-> Generate two file image: sin_s1.jpg, sin_s2.jpg (result)

Problem 2:
- B1: Run file Generator.py ta thu duoc 12 file wav:

	- C3.wav C3#.wav D3.wav D3#.wav E3.wav F3.wav F3#.wav G3.wav G3#.wav A3.wav A3#.wav B3.wav
	
- B2: Run file Player.py
- B3: Nhập vào số thự tự để play file wav (0 -> 12)

Problem 3:
1. Convert to grayscale
- B1: open file original image
- B2: convert to grayscale with function Image.convert('L')
- B3: Save file image with file name is color_to_grayscale.jpg

2. Split to three file of three channels is R, G, B (not found channel A)
- B1: Open file original image
- B2: Split image with function Image.Image.split()
- B3: Save file image with file name: red_image.png, green_image.png, blue_image.png
- B4: Check mode của file with function img.mode()

       - if mode == 'RGBA'-> save file image with file name: anpha_image.png

3. Merge from three file of three channels is R, G, B to the original image
- B1: Open three file image of three channels R, G, B
- B2: Check exists of file image channel A
- B3: if exists:

      - Open three file image of channel A
      - Merge image with function Image.merge() (4 channels)
      else:
      - Merge image with function Image.merge() (3 channels)
      
- B4: Save file image with file name: image.png
- B5: Compare original image with image.png

Problem 4:
- B1: Run file script.py
--> Result: generate 4 file image
	2 file ảnh tần số của ảnh gốc
	
	- imag.png
	- real.png
	
	Ảnh phục hồi
	- recover.png
	
	Ảnh sau khi được phục hồi
	- reconstructed .png
	

Problem 5:
Thư viện sử dụng: numpy, matplotlib

	- Bàn cờ vua gồm các ô đen trắng đan xen: run file 51.py
	
	- Dải màu  biến đổi từ đỏ đến tím theo chiều ngang: run 52.py
	  
	- Dải màu  biến đổi từ đỏ đến tím theo chiều dọc: run 53.py
	
	- Dải màu  biến đổi từ đỏ đến tím theo chiều chéo: run 54.py
	
Problem 6:
1. Linear-convolution
- B1: Run file linear.py
- B2: Input data of vecto x (ex: 1 0 0 1 8 2)
- B3: Input data of vecto y (ex: 1 0 1)
- B4: Result of linear-convolution: [1, 0, 1, 1, 8, 3, 8, 2]
- B5: Compare result by method convolve() in python
	* Solution 1:
	1. import numpy as np
	2. Call function: np.convolve(x, y)
	3. Compare result
	
	* Solution 2:
	1. from scipy import signal
	2. Call function: signal.convolve(x, y)
	3. Compare result

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
