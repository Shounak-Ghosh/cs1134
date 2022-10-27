def list_min(lst, low, high):
    if len(lst) == 0:  # edge case, empty list
        return None
    if high > len(lst) - 1 or low < 0:  # edge case, params are out of bounds
        raise ValueError("parameters out of bounds")

    if low == high:  # base case, only one element between low, high
        return lst[low]
    else:
        min = list_min(lst, low+1, high)  # recursive call, increment low by 1
        if lst[low] < min:  # if current element is less than min, return it
            return lst[low]
        else:
            return min


def list_min2(lst, low, high):
    if len(lst) == 0:  # base case, empty list
        return None
    if high > len(lst) - 1 or low < 0:  # edge case, params are out of bounds
        raise ValueError("high is out of bounds")
    if low == high:
        return lst[low]
    else:
        return min(lst[low], list_min2(lst, low + 1, high))


def main():
    print(list_min([2, 3, 1, 4, 5], 0, 4))
    print(list_min2([2, 3, 1, 4, 5], 0, 4))

    print(list_min([], 0, 0))
    print(list_min2([], 0, 0))

    print(list_min([1], 0, 0))
    print(list_min2([1], 0, 0))


if __name__ == '__main__':
    main()
