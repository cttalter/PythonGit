letter_list = list('abcdefghijklmnopqrstuvwxyz')
code_dict = {}
for i in range(26):
    code_dict[str(i + 1)] = letter_list[i]
keys = code_dict.keys()


def decode2(s):
    str0 = str(s)
    if len(str0) == 1:
        if str0 in keys:
            return 1
        else:
            return 0
    if str0[0] in keys:
        if str0[:2] in keys:
            if len(str0) == 2:
                return 2
            else:
                return decode2(int(str0[1:])) + decode2(int(str0[2:]))
        else:
            return decode2(int(str0[1:]))
    else:
        return 0


print(decode2(3212453259123))
