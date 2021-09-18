def stair(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return stair(x-1) + stair(x-2)


print(stair(3))
