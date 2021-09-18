def fibonacci(x):
    """计算Fibonacci数列第n项"""
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


if __name__ == '__main__':
    from datetime import datetime

    start = datetime.now()
    print(fibonacci(35))
    print(datetime.now() - start)
