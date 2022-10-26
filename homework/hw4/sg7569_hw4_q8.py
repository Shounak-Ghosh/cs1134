# given a nested list of integers, return an un-nested list of integers
def flat_list(nested_lst, low, high):
    if low == high:  # base case, only one element
        if type(nested_lst[low]) == int:  # check if it's an int
            return [nested_lst[low]]  # return a list with the int
        else:  # need to recurse and break down the the nested list
            return flat_list(nested_lst[low], 0, len(nested_lst[low])-1)
    else:
        if type(nested_lst[low]) == int:  # check if it's an int
            return [nested_lst[low]] + flat_list(nested_lst, low+1, high)
        else:
            return flat_list(nested_lst[low], 0, len(nested_lst[low])-1) + flat_list(nested_lst, low+1, high)


def main():
    nested_list = [[1, 2], 3, [4, [5, 6, [7], 8]]]
    print(nested_list)
    print(flat_list(nested_list, 0, 2))


if __name__ == '__main__':
    main()
