def padding(x, n):
    for i in range(n):
        x.append(0)

print("Input data of vecto x:", end=" ")
x = list(map(int, input().split()))
print("Input data of vecto y:", end=" ")
y = list(map(int, input().split()))

print("Input period:", end=" ")

n = int(input())
m = max(len(x), len(y))
z = []

if(len(x) < len(y)):
    padding(x, m - len(x))
else:
    padding(y, m - len(y))
    
padding(z, n)

for i in range(n, m):
    x[i % n] += x[i]
    y[i % n] += y[i]
    
for i in range(n):
    for j in range(n):
        z[i] += x[j] * y[(i - j + n) % n]

print("Result of cyclic-convolution:", end=" ")
print(z)
