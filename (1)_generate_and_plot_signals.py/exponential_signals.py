import math
import matplotlib.pyplot as plt
x = range(0, 15)
y = []
_y = []
# a > 1 or 0 < a < 1
a = .5
_a = 1.5
for i in x:
    y.append(a ** i)

for i in x:
    _y.append(_a ** i)

fig = plt.figure(0)
fig.canvas.set_window_title('Exponential Signal')

plt.subplot(1, 2, 1)
plt.plot(x, _y)
plt.title('a > 1, a = 1.5')

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title('0 < a < 1, a = .5')

plt.show()
