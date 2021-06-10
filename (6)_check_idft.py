import numpy as np
from scipy.fftpack import fft, ifft

x = [0, 1, 2, 3]
X = fft(x, 4)
print(X)
print(ifft(X))
