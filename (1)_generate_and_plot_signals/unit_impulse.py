import matplotlib.pyplot as plt

y = [0] * 21
y[10] = 1.0

x = []
for b in range(-10, 11):
    x.append(b)

plt.grid(True, which='both')
plt.stem(x, y)
plt.title('Unit Impulse Signal')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.show()
