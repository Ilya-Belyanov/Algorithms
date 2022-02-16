def rSum(massive):
    return 0 if not massive else massive[0] + rSum(massive[1:])


def lSum(massive):
    count = 0
    for i in massive:
        count += i
    return count


def swap(massive, i, j):
    memory_i = massive[i]
    massive[i] = massive[j]
    massive[j] = memory_i
    return massive
