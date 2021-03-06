# auto_correlation calculate
def auto_correlation(x, y, index_pos_x):
    length_x = len(x)
    length_y = len(y)

    ac_total_length = length_x + length_y - 1

    positive_index_x = length_x - index_pos_x - 1
    positive_index_y = index_pos_x
    ans_index_positive = positive_index_x + positive_index_y

    result_indexes = []
    for i in range(-(ac_total_length - ans_index_positive - 1), ans_index_positive + 1):
        result_indexes.append(i)
    ac = [0] * ac_total_length

    for i in enumerate(x):
        for j in enumerate(y):
            _i = i[0]
            _j = j[0]
            ac[_i + _j] = ac[_i + _j] + x[_i] * y[_j]

    return ac, result_indexes


num = input("Give the values of signal x(n): ")
x = [int(i) for i in num.split()]
index_pos_x = input(f"Initial index postion for x(n) (0-{len(x)-1}): ")

# x_axis[::-1] -> means reverse array
arr, result_indexes = auto_correlation(
    x, x[::-1], int(index_pos_x))

print('\n')
for i in range(len(arr)):
    print(f'x({result_indexes[i]})={arr[i]}')

print('\nArray of auto-correlation result : ', arr)
print('Resultant indexes                  : ', result_indexes)
