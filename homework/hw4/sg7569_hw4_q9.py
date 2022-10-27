def permutations(lst, low, high):
    if len(lst) == 0:  # edge case, empty list
        return lst
    if high > len(lst) - 1 or low < 0:  # edge case, params are out of bounds
        raise ValueError("parameters out of bounds")
    if low == high: # base case, only one element, only one permutation
        return [[lst[low]]]
    perms = permutations(lst, low+1, high) # get all permutations of the rest of the list
    new_perms = []  # list to hold all the new permutations with the lst[low] elemment
    
    for perm in perms: # for each existing permutation
        for i in range(len(perm)+1): # drop lst[low] in every possible position
            new_perms.append(perm[:i] + [lst[low]] + perm[i:])
    return new_perms # can use sorted() to order the permutations in ascending order


def main():
    lst1 = [1, 2, 3, 4]
    print(permutations(lst1, 1, len(lst1) - 1))


if __name__ == '__main__':
    main()
