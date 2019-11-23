#functions
def padding(u, n):
    for i in range(n): 
        u.append(0)

#main
print("Input data of vecto x:", end=" ")
x = list(map(int, input().split()))
print("Input data of vecto y:", end=" ")
y = list(map(int, input().split()))

z = []
t = []
n = len(x) + len(y) - 1
padding(y, n - len(y))
padding(z, n)

#Caculate liner-convolution
for i in range(len(x)):
    for j in range(n):
        z[j] += x[i] * y[(j - i + n) % n]

print("Result of linear-convolution:", end = " ")
print(z)

#Convert linear to cyclic
print("Convert linear-convolution to cyclic-convolution")
print("Input period of cyclic-convolution:", end=" ")

cyc = int(input())
padding(t, cyc)
for i in range(len(z)):
    t[i % cyc] += z[i]

print("Result of cyclic-convolution:", end=" ")
print(t)