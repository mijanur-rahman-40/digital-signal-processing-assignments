# convolution calculate
def linear_convolution(x, h, index_pos_x, index_pos_h):
    length_x = len(x)
    length_h = len(h)
    convolution_total_length = length_x + length_h - 1
    positive_index_x = length_x - index_pos_x - 1
    positive_index_h = length_h - index_pos_h - 1
    ans_index_positive = positive_index_x + positive_index_h

    result_indexes = []
    for i in range(-(convolution_total_length - ans_index_positive - 1), ans_index_positive + 1):
        result_indexes.append(i)

    c = [0] * convolution_total_length
    for i in enumerate(x):
        for j in enumerate(h):
            _i = i[0]
            _j = j[0]
            c[_i + _j] = c[_i + _j] + x[_i] * h[_j]

    return c, result_indexes


# x = [1, 2, 3, 1]
num = input("Give the values of signal x(n): ")
x = [int(i) for i in num.split()]
index_pos_x = input(f"Initial index postion for x(n) (0-{len(x)-1}): ")

# h = [1, 2, 1, -1]
num = input("Give the values of signal h(n): ")
h = [int(i) for i in num.split()]
index_pos_h = input(f"Initial index postion for h(n) (0-{len(h)-1}): ")

arr, result_indexes = linear_convolution(
    x, h, int(index_pos_x), int(index_pos_h))

print('\n')
for i in range(len(arr)):
    print(f'y({result_indexes[i]}) = {arr[i]}')

print('\nArray of linear_convolution result y(n) : ', arr)
print('Resultant indexes                         : ', result_indexes)
