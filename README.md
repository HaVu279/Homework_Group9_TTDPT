# Homework_Group9_TTDPT
Problem 1:

Problem 2:

Problem 3:

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
