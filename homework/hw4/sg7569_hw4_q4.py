def list_min(lst, low, high):
    if low == high:  # base case, only one element between low, high
        return lst[low]
    else:
        min = list_min(lst, low+1, high)  # recursive call, increment low by 1
        if lst[low] < min:  # if current element is less than min, return it
            return lst[low]
        else:
            return min


def list_min2(lst, low, high):
    if low == high:
        return lst[low]
    else:
        return min(lst[low], list_min2(lst, low + 1, high))
