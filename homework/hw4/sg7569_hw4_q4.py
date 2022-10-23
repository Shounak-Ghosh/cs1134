def list_min(lst, low, high):
    if low == high:
        return lst[low]
    else:
        return min(lst[low], list_min(lst, low + 1, high))