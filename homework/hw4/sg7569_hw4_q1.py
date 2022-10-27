def sum_lst1(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        print(lst)
        rest = sum_lst1(lst[1:])
        sum = lst[0] + rest
        return sum


def sum_lst2(lst, low, high):
    if low == high:
        return lst[low]
    else:
        rest = sum_lst2(lst, low+1, high)
        sum = lst[low] + rest
        return sum


def main():
    lst = [1, 2, 3, 4, 5]
    print(sum_lst1(lst))
    print(sum_lst2(lst, 0, 4))
    print(lst[len(lst) - 2:])


if __name__ == '__main__':
    main()
