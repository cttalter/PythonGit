record = {0: 0, 1: 1}  # record computed outcome


def fibonacci(x):
    """计算Fibonacci数列第n项"""
    if x not in record.keys():
        record[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return record[x]


if __name__ == '__main__':
    from datetime import datetime  # calculate time
    import sys

    sys.setrecursionlimit(2000000)
    start = datetime.now()
    for i in range(1, 301):
        fibonacci(i * 2000)
    print(fibonacci(600000))
    print(datetime.now() - start)
