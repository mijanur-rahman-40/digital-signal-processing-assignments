# fir filter by means of dft and idft
def fir_filter(x, y):
    length_x = len(x)
    length_y = len(y)
    total_length = length_x + length_y - 1

    filters = [0] * total_length
    for i in enumerate(x):
        for j in enumerate(y):
            _i = i[0]
            _j = j[0]
            filters[_i + _j] = filters[_i + _j] + x[_i] * y[_j]

    return filters


print('\nResponse will be like linear convolution by means of DFT and IDFT\n')

# x = [1, 2, -1, 5, 6]

num = input("Give the values of signal x(n): ")
x = [int(i) for i in num.split()]

# h = [5, 6, 7]
num = input("Give the values of signal h(n): ")
h = [int(i) for i in num.split()]

print('Array of filters result: ', fir_filter(x, h))
