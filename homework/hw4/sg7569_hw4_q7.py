def split_by_sign(lst, low, high):
    if low == high:
        return [lst[low]]
    else:
        if lst[low] < 0:
            return [lst[low]] + split_by_sign(lst, low+1, high)
        else:
            return split_by_sign(lst, low+1, high) + [lst[low]]

def main():
    lst = [-1, 2, -3, 4, -5, 6, -7, 8]
    print(lst)
    print(split_by_sign(lst, 0, len(lst)-1))

if __name__ == '__main__':
    main()