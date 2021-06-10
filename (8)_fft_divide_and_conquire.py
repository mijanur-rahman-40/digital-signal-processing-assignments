import math

def fast_fourier_transform(x):
    n = len(x)

    if n == 1:
        return x

    left_side = [num for i, num in enumerate(x) if i % 2 == 0]
    right_side = [num for i, num in enumerate(x) if i % 2 == 1]

    transformed_left = fast_fourier_transform(left_side)
    transformed_right = fast_fourier_transform(right_side)

    inverted_root = math.e ** (2 * math.pi * 1j / n)
    root = 1

    results = [0] * n
    for i in range(0, int(n/2)):
        results[i] = transformed_left[i] + root * transformed_right[i]
        results[int(i + n/2)] = transformed_left[i] - \
            root * transformed_right[i]
        root = root * inverted_root
    return results


num = input("Give the values of signal x(n): ")
x = [int(i) for i in num.split()]
# x = [0, 18, -15, 3]

X = fast_fourier_transform(x);
for i in range(len(X)):
    print(f'X[{i}]: {X[i]}')

