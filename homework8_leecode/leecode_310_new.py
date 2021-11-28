import copy


def findMinHeightTrees(n: int, edges: list[int]):
    """find pot which only appear 1 time in edges, delete all branches including these, delete all pots from pot_list
    do it until pot list left 1 or 2 pot, record times, that's the depth"""
    pot_list = list(range(n))
    edges_copy = copy.deepcopy(edges)
    while len(pot_list) > 2:
        cut_pot_list = []
        for i in pot_list:
            time = 0
            for branch in edges_copy:
                if i in branch:
                    time += 1
                if time > 1:
                    break
            if time == 1:
                cut_pot_list.append(i)
        for pot in cut_pot_list:
            for branch in edges_copy:
                if pot in branch:
                    edges_copy.remove(branch)
        pot_list = set(pot_list)
        pot_list.difference_update(set(cut_pot_list))
        pot_list = list(pot_list)
    return pot_list


n0 = 8
edges0 = [[0, 1], [0, 2], [2, 3], [3, 4], [2, 5], [5, 6], [1, 7]]
print(findMinHeightTrees(n0, edges0))
