def two_sum(srt_lst, target):
    # define pointers at opposite ends of the list
    low = 0
    high = len(srt_lst) - 1

    while low < high:
        if srt_lst[low] + srt_lst[high] == target:  # target found
            return (low, high)
        elif srt_lst[low] + srt_lst[high] < target:  # sum too small, increment low
            low += 1
        else:  # sum too large, decrement high
            high -= 1

    return None


def main():
    srt_lst = [-2, 7, 11, 15, 20, 21]
    target = 22
    print(two_sum(srt_lst, target))


if __name__ == "__main__":
    main()
