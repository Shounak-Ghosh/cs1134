def split_parity(lst, low, high):
    if low >= high:
        return
    if lst[low] % 2 == 1: # move odd numbers to the back of the list
        lst[low], lst[high] = lst[high], lst[low]
        split_parity(lst, low, high-1) # lst[high] is now in the right place, move down one
    else: # low is even, move on to the next element
        split_parity(lst, low+1, high)

def nested_sum(lst):
    if len(lst) == 0: # base case, empty list
        return 0
    elif type(lst[0]) == int: # first element is an int
        return lst[0] + nested_sum(lst[1:])
    else: 
        return nested_sum(lst[0]) + nested_sum(lst[1:])

def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    split_parity(lst, 0, len(lst)-1)
    print(lst)

    nested_list = [1, 2, [3, 4, [5, 6, 7], 8], 9, 10]
    print(nested_sum(nested_list))

if __name__ == '__main__':
    main()
