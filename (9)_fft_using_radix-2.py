
import math
import cmath


class Radix2:

    def __init__(self, n):
        self.N = n
        self.stages = int(math.log(self.N, 2))
        self.xn = [0 + 0j] * self.N
        self.xn1 = self.xn.copy()
        self.XN = self.xn.copy()

        # Twiddle Factor
        self.w = cmath.exp((-1j) * 2 * math.pi / self.N)
        self.W = []
        for i in range(int(self.N / 2)):
            self.W.append(self.w ** i)

    def reverse_bits(self, n):
        result = 0
        for i in range(self.stages):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

    def inputs(self, inputs):
        for i in range(len(inputs)):
            self.xn[i] = complex(inputs[i])
            self.xn1[self.reverse_bits(i)] = self.xn[i]

    def print_values(self):
        print('\nOutput X(N):')
        for i in range(len(self.XN)):
            print('X[', i, ']:', self.XN[i])

    def run(self):
        for i in range(1, self.stages + 1):
            xn_tmp = [0 + 0j] * self.N

            for j in range(0, self.N, 2 ** i):
                index_array = []
                for k in range(j, j + 2 ** i):
                    index_array.append(k)

                mid_point = index_array.__len__() // 2
                power = 0
                step = math.log(self.N, 2) - (i - 1)

                for m in range(mid_point):
                    xn_tmp[index_array[m]] = \
                        self.xn1[index_array[m]] + (self.w ** power) * \
                        self.xn1[index_array[m + mid_point]]

                    xn_tmp[index_array[m + mid_point]] = \
                        self.xn1[index_array[m]] - (self.w ** power) * \
                        self.xn1[index_array[m + mid_point]]
                    power += step

            self.xn1 = xn_tmp.copy()
        self.XN = self.xn1.copy()

    def result(self):
        return self.XN


print('\nN = 8')
radix = Radix2(8)

# x = [1, 2, 4, 8, 16, 32, 64, 128]

num = input("Give the 8 values of signal x(n): ")
x = [int(i) for i in num.split()]
radix.inputs(x)
radix.run()
radix.print_values()
