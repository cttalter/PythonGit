import copy


def permute(nums_list):
    num1 = nums_list[0]  # take first number for core
    nums_list.pop(0)
    last_list = [[num1]]
    return_list = []
    for num in nums_list:  # put each num into lists' gap to make new lists
        for per_list in last_list:
            for i in range(len(per_list) + 1):
                list_copy = per_list[:]
                list_copy.insert(i, num)
                return_list.append(list_copy)
        last_list = copy.deepcopy(return_list)
        return_list = []
    return last_list


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    print(permute(a))
