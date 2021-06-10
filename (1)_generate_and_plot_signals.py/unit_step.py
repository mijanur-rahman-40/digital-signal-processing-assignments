import matplotlib.pyplot as plt

y = [0] * 21

x = []

for b in range(-10, 11):
    if b >= 0:
        y[b + 10] = 1
    x.append(b)


plt.grid(True, which='both')
plt.stem(x, y)
plt.title('Unit Step Signal')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.show()
