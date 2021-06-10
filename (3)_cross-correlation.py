# cross_correlation calculate
def cross_correlation(x, y, index_pos_x, index_pos_y):
    length_x = len(x)
    length_y = len(y)

    cc_total_length = length_x + length_y - 1

    positive_index_x = length_x - index_pos_x - 1
    positive_index_y = index_pos_y
    ans_index_positive = positive_index_x + positive_index_y

    result_indexes = []
    for i in range(-(cc_total_length - ans_index_positive - 1), ans_index_positive + 1):
        result_indexes.append(i)
    cc = [0] * cc_total_length

    for i in enumerate(x):
        for j in enumerate(y):
            _i = i[0]
            _j = j[0]
            cc[_i + _j] = cc[_i + _j] + x[_i] * y[_j]

    return cc, result_indexes


x = [2, -1, 3, 7, 1, 2, -3]
# num = input("Give the values of signal x(n): ")
# x = [int(i) for i in num.split()]
index_pos_x = input(f"Initial index postion for x(n) (0-{len(x)-1}): ")

y = [1, -1, 2, -2, 4, 1, -2, 5]
# num = input("Give the values of signal y(n): ")
# y = [int(i) for i in num.split()]
index_pos_y = input(f"Initial index postion y(n) (0-{len(y)-1}): ")

print('\n')

arr, result_indexes = cross_correlation(
    x, y[::-1], int(index_pos_x), int(index_pos_y))

for i in range(len(arr)):
    print(f'rxy({result_indexes[i]}) = {arr[i]}')

print('\nArray of cross-correlation result: ', arr)
print('Resultant indexes                : ', result_indexes)


