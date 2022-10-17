def remove_all(lst, val):
    new_index = 0  # pointer
    val_count = 0

    # "skip over" all occurences of val by only incrementing new_index when non_val element is seen
    for i in range(len(lst)):
        if lst[i] != val:
            lst[new_index] = lst[i]
            new_index += 1
        else:  # count all appearances of val for later
            val_count += 1

    # remove last_val_count elements from lst, these have already been pushed forward
    for i in range(val_count):
        lst.pop()  # amortized O(1) pop, final O(n) runtime

    return lst


def main():
    lst = [1, 2, 3, 4, 4, 3, 2, 1]
    print(remove_all(lst, 3))


if __name__ == '__main__':
    main()
