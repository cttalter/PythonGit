def fibonacci(x):
    """计算Fibonacci数列第n项"""
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)


if __name__ == '__main__':
    from datetime import datetime
    import sys

    sys.setrecursionlimit(60000)
    start = datetime.now()
    print(fibonacci(1000))
    print(datetime.now() - start)
