class List:
    def __init__(self, list_source):
        self.list0 = list_source

    def index(self, index0):
        return self.list0[index0]

    def cut(self, index1, index2):
        returns = []
        for i in range(index1, index2 + 1):
            returns.append(self.list0[i])
        return returns

    def __add__(self, other):
        result_list = self.list0[:]
        for element in other.list0:
            result_list.append(element)
        return List(result_list)

    def lenth(self):
        return len(self.list0)

    def maximum(self):
        max0 = self.list0[0]
        for element in self.list0:
            if element > max0:
                max0 = element
        return max0

    def minimum(self):
        min0 = self.list0[0]
        for element in self.list0:
            if element < min0:
                min0 = element
        return min0

    def delete(self, index0):
        self.list0 = self.list0[:index0] + self.list0[index0 + 1:]

    def append(self, element):
        self.list0 += [element]

    def extend(self, iter0):
        for i in iter0:
            self.append(i)

    def count(self, element):
        times = 0
        for i in self.list0:
            if i == element:
                times += 1
        return times

    def index_find(self, target, *index0):
        if len(index0) == 0:
            for i in range(self.lenth()):
                if self.list0[i] == target:
                    return i
            return 'None'
        elif len(index0) == 1:
            for i in range(index0[0], self.lenth()):
                if self.list0[i] == target:
                    return i
            return 'None'
        elif len(index0) == 2:
            for i in range(index0[0], index0[1]):
                if self.list0[i] == target:
                    return i
            return 'None'

    def insert(self, index0, element):
        self.list0 = self.list0[:index0] + [element] + self.list0[index0:]

    def reserve(self):
        new_list = []
        for i in range(self.lenth()-1, -1, -1):
            new_list.append(self.list0[i])
        self.list0 = new_list


test0 = List([2, 45, 1, 3, 66, 9])
print(test0.list0)
print(test0.index(3))
print(test0.cut(2, 4))
test1 = List([99, 4])
test2 = test1 + test0
print(test2.list0)
print(test2.lenth())
print(test2.maximum())
print(test2.minimum())
test2.delete(3)
print(test2.list0)
test2.append(45)
print(test2.list0)
list_extend = [1, 2, 3]
test2.extend(list_extend)
print(test2.list0)
print(test2.count(2))
print(test2.index_find(2, 3, 6))
test2.insert(3, 555)
print(test2.list0)
test2.reserve()
print(test2.list0)
