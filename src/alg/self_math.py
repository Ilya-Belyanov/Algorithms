from numba import njit, int64


@njit(int64(int64))
def factorial_r(number: int64):
    return 1 if number == 0 else number * factorial_r(number - 1)


@njit(int64(int64), locals={'count': int64})
def factorial_l(number: int64) -> int64:
    count = 1
    for i in range(1, number + 1):
        count *= i
    return count
