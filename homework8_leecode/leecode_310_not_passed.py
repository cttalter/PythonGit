import copy


def findMinHeightTrees(n: int, edges: list[int]):
    """calculate every pot's depth, find max
    to every pot, delete all root including it from source_list, record every another pot as next floor pot
    record depth until source_list is empty"""
    height_dict = {}  # record every pot's height
    for i in range(n):
        each_height = 0  # each_height : height of each pot
        source_list = copy.deepcopy(edges)
        root_set = {i}  # hold next floor pot
        while source_list:
            hold_list = []  # hold root to delete from source_list
            for each_list in source_list:
                for each_root in root_set:
                    if each_root in each_list:
                        hold_list.append(each_list)
                        break
            root_set = set()  # clear to hold next floor pot
            for each_list in hold_list:
                source_list.remove(each_list)
                root_set.update(set(each_list))
            each_height += 1
        height_dict[i] = each_height
    min_height = min(height_dict.values())
    pot_list = []
    for pot in height_dict.keys():
        if height_dict[pot] == min_height:
            pot_list.append(pot)
    return pot_list


n0 = 8
edges0 = [[0, 1], [0, 2], [2, 3], [3, 4], [2, 5], [5, 6], [1, 7]]
print(findMinHeightTrees(n0, edges0))
