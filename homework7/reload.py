class ListCalculate(list):
    def __sub__(self, other):
        return_list = self[:]
        for element in other:
            if element in return_list:
                return_list.remove(element)
        return return_list

    def __mul__(self, other):
        return_list = self[:]
        if len(self) >= len(other):
            for i in range(len(other)):
                return_list.insert(2*i+1, other[i])
        else:
            for i in range(len(self)):
                return_list.insert(2*i+1, other[i])
            return_list.append(other[len(self)+1:])
        return return_list

    def __truediv__(self, other):
        return_list = self[:]
        other = list(set(other))
        for element in other:
            if element in return_list:
                while element in return_list:
                    return_list.remove(element)
            else:
                return_list.append(element)
        return return_list


b = [1, 2, 4, 2, 5, 9, 8, 9]
a = [4, 5, 6, 7, 8]
a1 = ListCalculate(a)
b1 = ListCalculate(b)
print(a1 + b1)
print(a1 - b1)
print(a1 * b1)
print(a1 / b1)
