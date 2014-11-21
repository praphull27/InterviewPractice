def intersection (list1, list2):
    list1_dict = {}
    for item in list1:
        if item in list1_dict:
            list1_dict[item] += 1
        else:
            list1_dict[item] = 1
    common = []
    for item in list2:
        if (item in list1_dict) and (list1_dict[item] != 0):
            list1_dict[item] -= 1
            common.append(item)
    return common
