letter_list = list('abcdefghijklmnopqrstuvwxyz')
code_dict = {}
for i in range(26):
    code_dict[str(i + 1)] = letter_list[i]


def cut(x):
    if (x.find('1') == -1 and x.find('2') == -1) or len(x) == 1:
        return []
    else:
        cut_start = min(x.find('1'), x.find('2')) if min(x.find('1'), x.find('2')) >= 0 else max(x.find('1'),
                                                                                                 x.find('2'))
        cut_end = cut_start + 1
        while x[cut_end] in ['1', '2']:
            if cut_end == len(x) - 1:
                break
            cut_end += 1
        outstr = x[cut_start:cut_end + 1]
        return [outstr] + cut(x[cut_end + 1:])


def count(x):
    if len(x) == 1:
        return 1
    if x[-2] == '2' and int(x[-1]) > 6:
        return count(x[:-1])
    else:
        if len(x) == 2:
            return 2
        else:
            return count(x[1:]) + count(x[2:])


def count_all(x):
    x = str(x)
    cut_list = cut(x)
    times = 1 if x != '0' else 0
    for string in cut_list:
        times = times * count(string)
    return times


print(count_all(3212453259123))
