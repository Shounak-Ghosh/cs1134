def shift(lst, k, dir='left'):
    # shifts original list by k positions to the left
    if dir == 'left':
        return lst[k:] + lst[:k]
    elif dir == 'right':
        return lst[-k:] + lst[:-k]


def main():
    lst = [1, 2, 3, 4, 5, 6]
    print(shift(lst, 2))
    print(shift(lst, 2, 'right'))

if __name__ == '__main__':
    main()
