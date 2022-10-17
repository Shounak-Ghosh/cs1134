def find_duplicates(lst):
    n = len(lst)
    count_arr = [0] * n

    # count_arr stores a tally of the number of times each element of lst appears
    for i in range(n):
        count_arr[lst[i]] += 1

    dup_count = 0
    for i in range(n):  # find the number of duplicates
        if count_arr[i] > 1:
            dup_count += 1

    duplicates = [0] * dup_count  # preallocate space for duplicates
    dup_count = 0  # use as duplicate array index
    for i in range(n):
        if count_arr[i] > 1:
            duplicates[dup_count] = i
            dup_count += 1
    return duplicates


def main():
    lst = [2, 4, 4, 1, 2]
    print(find_duplicates(lst))


if __name__ == '__main__':
    main()
