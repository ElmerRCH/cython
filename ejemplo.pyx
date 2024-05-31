
def sum_of_squares(int n):
    print('llego cython')
    cdef int total = 0
    cdef int i
    for i in range(n):
        total += i * i
    return total