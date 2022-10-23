def positive_prefix_sum(lst):
    return [i for i in range(len(lst)) if sum(lst[:i+1]) > 0]

def remove_all_evens(lst):
    nindex = 0
    ecounter = 0

    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            ecounter += 1
        else:
            lst[nindex] = lst[i]
            nindex += 1
    
    for i in range(ecounter):
        lst.pop()
    
    return lst

def is_sorted(lst, low, high):
    if low >= high:
        return True
    if lst[low] > lst[high]:
        return False
    
    return is_sorted(lst, low+1, high)

def main():
    print(positive_prefix_sum([1, 2, -3000, 4, 5, -6, 7, 8, -9, 10]))

    print(remove_all_evens([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

    print(is_sorted([100, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9))

if __name__ == '__main__':
    main()
