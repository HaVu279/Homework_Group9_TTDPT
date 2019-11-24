import numpy as np
import math
from matplotlib import pyplot as plt

# Cho trước các thông số (khai báo thành các biến)
A = 1  # Biên độ của tín hiệu cơ bản
f = 60	# Tần số cơ bản
fs = 1/1000  # Tần số lấy mẫu
N = 5 # số chu kỳ tín hiệu cần vẽ tính với tần số cơ bản f
n = 2000

# + Vẽ đồ thị dạng sóng (theo thời gian) của tín hiệu:
#      s1(t) = A sin(2pi f t)
T = 1/f # Chu kỳ
t = np.arange(0, N * T,N * T / (1/fs) ) # Thời gian t
s1 = A * np.sin(2 * math.pi * f * t)  # Tín hiệu s1

fig = plt.figure()
plt.plot(t, s1)
fig.savefig('sin_s1.jpg')

# + Vẽ đồ thị dạng sóng (theo thời gian) của tín hiệu s2(t)
s2 = A * np.sin(2 * math.pi * f * t)
for i in range(1, 2*n + 2):
    A = A/math.pow((2*i + 1), 2)
    s2 += A * np.sin(2 * math.pi * (2*i + 1) * f * t)

fig = plt.figure()
plt.plot(t, s2)
fig.savefig('sin_s2.jpg')
