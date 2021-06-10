import math
from scipy.fftpack import fft, ifft
from dft_5 import DFT


def IDFT(dft_regular, dft_imaginary):
    index_range_len = len(dft_regular)
    idft_regular, idft_imaginary = [], []

    for n in range(index_range_len):
        idft_regular_value, idft_imaginary_value = 0.0, 0.0
        for k in range(index_range_len):
            v_re = dft_regular[k] \
                * (math.cos((2 * math.pi / index_range_len) * k * n)) \
                - dft_imaginary[k] \
                * (math.sin((2 * math.pi / index_range_len) * k * n))
            v_im = dft_regular[k] \
                * (math.sin((2 * math.pi / index_range_len) * k * n)) \
                + dft_imaginary[k] \
                * (math.cos((2 * math.pi / index_range_len) * k * n))
            idft_regular_value += v_re
            idft_imaginary_value += v_im

        idft_regular_value /= index_range_len
        idft_imaginary_value /= index_range_len

        idft_regular.append(round(idft_regular_value))
        idft_imaginary.append(round(idft_imaginary_value))

    return idft_regular, idft_imaginary

num = input("Give the values of signal x(n): ")
x = [int(i) for i in num.split()]
dft_re_array, dft_im_array = DFT(x)


idft_regular, idft_imaginary = IDFT(dft_re_array, dft_im_array)

print("\nInverse Discreate Fourier Transform (without libray): \n")
for i in range(len(idft_regular)):
    print(f'X[{i}] : ({idft_regular[i]} {idft_imaginary[i]}j)')

X = fft(x, len(x))
print("\nInverse Discreate Fourier Transform (using libray):\n")
print(ifft(X))

print("\nAnswer is same for both cases\n")


