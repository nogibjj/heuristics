"""
From numba documentation: 
https://numba.pydata.org/numba-doc/latest/cuda/examples.html#matrix-multiplication
"""

from numba import cuda, float32
import numpy as np
from timeit import default_timer as timer

# Controls threads per block and shared memory usage.
# The computation will be done on blocks of TPBxTPB elements.
TPB = 16

@cuda.jit
def fast_matmul(A, B, C):
    # Define an array in the shared memory
    # The size and type of the arrays must be known at compile time
    sA = cuda.shared.array(shape=(TPB, TPB), dtype=float32)
    sB = cuda.shared.array(shape=(TPB, TPB), dtype=float32)

    x, y = cuda.grid(2)

    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    bpg = cuda.gridDim.x    # blocks per grid

    if x >= C.shape[0] and y >= C.shape[1]:
        # Quit if (x, y) is outside of valid C boundary
        return

    # Each thread computes one element in the result matrix.
    # The dot product is chunked into dot products of TPB-long vectors.
    tmp = 0.
    for i in range(bpg):
        # Preload data into shared memory
        sA[tx, ty] = A[x, ty + i * TPB]
        sB[tx, ty] = B[tx + i * TPB, y]

        # Wait until all threads finish preloading
        cuda.syncthreads()

        # Computes partial product on the shared memory
        for j in range(TPB):
            tmp += sA[tx, j] * sB[j, ty]

        # Wait until all threads finish computing
        cuda.syncthreads()

    C[x, y] = tmp

# run it
if __name__ == '__main__':

    # Initialize the data arrays
    A = np.full((TPB*20, TPB*20), 3, np.float32)
    B = np.full((TPB*20, TPB*20), 4, np.float32)

    # Configure the blocks
    threadsperblock = (TPB, TPB)
    blockspergrid_x = int(np.ceil(A.shape[0] / threadsperblock[0]))
    blockspergrid_y = int(np.ceil(B.shape[1] / threadsperblock[1]))
    blockspergrid = (blockspergrid_x, blockspergrid_y)

    # Start the kernel 
    C = np.zeros_like(A)
    start = timer()
    fast_matmul[blockspergrid, threadsperblock](A, B, C)
    cuda.synchronize()
    print("Time taken: %f" % (timer() - start))

    # Print the result
    print(C)