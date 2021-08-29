def fibonacci(x):
    """计算Fibonacci数列第n项"""
    if x <= 0 or not isinstance(x,int):
        print('x>0 and x is a integer')
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


print(fibonacci(6))
