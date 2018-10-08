from Gem import Gem

def merge_sort_by_count_punish(count_punish_list):
    if len(count_punish_list) <= 1:
        return count_punish_list
    list_mid = int(len(count_punish_list) / 2)
    left_list = merge_sort_by_count_punish(count_punish_list[:list_mid])
    right_list = merge_sort_by_count_punish(count_punish_list[list_mid:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    result_list = []
    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i].count_punish <= right_list[j].count_punish:
            result_list.append(left_list[i])
            i += 1
        else:
            result_list.append(right_list[j])
            j += 1
            Gem.change_count()
            Gem.compare_count()
    result_list += left_list[i:]
    result_list += right_list[j:]
    return result_list
