def split_by_sign(lst, low, high):
    if len(lst) == 0:  # edge case, empty list
        return lst
    if high > len(lst) - 1 or low < 0:  # edge case, params are out of bounds
        raise ValueError("parameters out of bounds")
    if low == high:
        return lst
    else:
        if lst[low] > 0:
            lst[low], lst[high] = lst[high], lst[low]
            return split_by_sign(lst, low, high - 1)
        else:
            return split_by_sign(lst, low+1, high)

def split_by_sign_iterative(lst, l, h):
    low = l
    high = h
    while low < high:
        if lst[low] > 0:
            lst[low], lst[high] = lst[high], lst[low]
            high -= 1
        else:
            low += 1
    return lst
 
def main():
    lst1 = [1, -1, 2, 4, 6, -6, -7]
    lst2 = [1, 1, 3]
    print(split_by_sign(lst1, 0, len(lst1) - 1))
    print(split_by_sign(lst1, 2, len(lst1) - 1))
    print(split_by_sign(lst2, 2, len(lst2) - 1))

    print(split_by_sign_iterative(lst1, 0, len(lst1) - 1))
    print(split_by_sign_iterative(lst1, 2, len(lst1) - 1))
    print(split_by_sign_iterative(lst2, 2, len(lst2) - 1))



if __name__ == '__main__':
    main()