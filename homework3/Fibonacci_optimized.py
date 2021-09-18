def fibonacci(x):
    """计算Fibonacci数列第n项"""
    record = {0: 0, 1: 1}  # record computed outcome
    if x not in record.keys():
        record[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return record[x]


if __name__ == '__main__':
    from datetime import datetime

    start = datetime.now()
    print(fibonacci(35))
    print(datetime.now() - start)
