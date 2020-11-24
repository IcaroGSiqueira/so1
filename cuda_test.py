import numpy as np
from numba import cuda

@cuda.jit
def add_2(array):
    pos = cuda.grid(1)
    array[pos] = array[pos] + 2

# criamos um vetor ordenado até 100000, [0, 1, 2, .. 999999]
an_array = np.arange(100000)

threadsperblock = 32
blockspergrid = (an_array.size + (threadsperblock - 1)) // threadsperblock

for x in range(1000):
    add_2[blockspergrid, threadsperblock](an_array)


print(an_array)