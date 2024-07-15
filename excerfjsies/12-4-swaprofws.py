import numpy as np
import copy

def swap_rows(M, a, b):
    M_copy = np.copy(M)
    M[a] = M_copy[b]
    M[b] = M_copy[a]

def swap_cols(M, a, b):
    M_copy = np.copy(M)
    M[:,a] = M_copy[:,b]
    M[:,b] = M_copy[:,a]

a = np.array([[1, 2, 3, 4, 5, 6], 
              [0, 9, 8, 7, 6, 5],
              [6, 2, 3, 7, 9, 2],
              [2, 7, 4, 9, 2, 5]])

print(swap_cols(a, 1, 2))
print(swap_rows(a, 1, 2))