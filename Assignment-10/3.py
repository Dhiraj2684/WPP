import numpy as np

def odd_magic_square(N):
    magic_square = np.zeros((N, N), dtype=int)
    i, j = 0, N // 2

    for num in range(1, N*N + 1):
        magic_square[i, j] = num
        new_i, new_j = (i - 1) % N, (j + 1) % N
        if magic_square[new_i, new_j] != 0:
            i += 1
        else:
            i, j = new_i, new_j
    return magic_square

def even_magic_square(N):
    magic_square = np.arange(1, N*N + 1).reshape(N, N)
    swap = np.zeros((N, N), dtype=bool)

    for i in range(N):
        for j in range(N):
            if (i % 4 == j % 4) or ((i + j) % 4 == 3):
                swap[i, j] = True

    selected_elements = magic_square[swap]
    magic_square[swap] = selected_elements[::-1]
    
    return magic_square

size = int(input("Enter the size of the magic square (N): "))
if size % 2 == 1:
    print(f"Magic Square for N = {size}:\n", odd_magic_square(size), "\n")
else:
    print(f"Magic Square for N = {size}:\n", even_magic_square(size), "\n")
