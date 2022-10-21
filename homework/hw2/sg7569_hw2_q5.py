def split_parity(lst):
    # define pointers at opposite ends of the list
    high = len(lst) - 1
    low = 0

    while low < high:
        if lst[low] % 2 == 1:  # move on if odd number at index low
            low += 1
        else:  # even number at index low, swap with high, decrement high
            lst[low], lst[high] = lst[high], lst[low]
            high -= 1
    return lst


def main():
    lst = [1, 2, 3, 4]
    print(split_parity(lst))


if __name__ == "__main__":
    main()
