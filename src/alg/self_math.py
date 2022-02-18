from numba import njit, int64


@njit(int64(int64))
def factorial_r(x: int64):
    return 1 if x == 0 else x * factorial_r(x - 1)


@njit(int64(int64), locals={'count': int64})
def factorial_l(x: int64) -> int64:
    count = 1
    for i in range(1, x + 1):
        count *= i
    return count
