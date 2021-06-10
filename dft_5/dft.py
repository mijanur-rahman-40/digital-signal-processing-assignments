
import math


def DFT(x):
    x_regular = x
    x_imaginary = []
    dft_regular, dft_imaginary = [], []

    index_range_len = len(x_regular)

    for i in range(len(x_regular)):
        x_imaginary.append(0.0)

    for k in range(index_range_len):
        dft_regular_value, dft_imaginary_value = 0.0, 0.0
        for n in range(index_range_len):
            value_regular = x_regular[n] \
                * (math.cos((2 * math.pi / index_range_len) * k * n)) \
                + x_imaginary[n] \
                * (math.sin((2 * math.pi / index_range_len) * k * n))
            value_imaginary = x_regular[n] \
                * (-math.sin((2 * math.pi / index_range_len) * k * n)) \
                + x_imaginary[n] \
                * (math.cos((2 * math.pi / index_range_len) * k * n))

            dft_regular_value += value_regular
            dft_imaginary_value += value_imaginary

        dft_regular.append(round(dft_regular_value))
        dft_imaginary.append(round(dft_imaginary_value))

    return dft_regular, dft_imaginary


if __name__ == "__main__":
    num = input("Give the values of signal x(n): ")
    x = [int(i) for i in num.split()]

    dft_re_array, dft_im_array = DFT(x)
    print("\nDiscreate Fourier Transform :")

    for i in range(len(dft_re_array)):
        print(f'X[{i}] : ({dft_re_array[i]} {dft_im_array[i]}j)')
