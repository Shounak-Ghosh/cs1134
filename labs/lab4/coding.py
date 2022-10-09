# 1
import re


def is_palindrome(s):
    # define pointers at opposite ends of the string
    low = 0
    high = len(s) - 1

    while low < high:
        # if the characters at the pointers are not equal, return False
        if s[low] != s[high]:
            return False
        # increment the low pointer and decrement the high pointer
        low += 1
        high -= 1
    
    # if the pointers cross, return True
    return True
# 2
def reverse_vowels(input_str):
    """
    : input_str type: string
    : return type: string
    """

    list_str = list(input_str) #list constructor guarantees Theta(n)
    vowels = ['a', 'e', 'i', 'o', 'u'] 
    low = 0
    high = len(list_str) - 1

    while low < high:
        # move pointers until they both to point to vowels
        if list_str[low] not in vowels: 
            low += 1
        elif list_str[high] not in vowels:
            high -= 1
        else:
            list_str[low], list_str[high] = list_str[high], list_str[low]
            low += 1
            high -= 1

    return "".join(list_str)

# 3a: theta(n^2)
# 3b
def find_missing(lst):
    """
    : nums type: list[int] (sorted)
    : return type: int
    """
    # define pointers at opposite ends of the list
    low = 0
    high = len(lst) - 1

    while low < high:
       mid = (low + high) // 2
       # found missing
       if lst[mid + 1] - lst[mid] > 1:
           return lst[mid] + 1
       # value and index are equal, missing is in higher half
       elif lst[mid] == mid: 
           low = mid + 1
       # value and index are not equal, missing is in lower half
       else:
         high = mid - 1
    
    # edge cases
    if lst[0] > 0: # 0 is missing
        return 0
    else: # last element is missing
         return len(lst)

      # 0 1 2 3 4 5 6 7 8 
      # 0 1 2 3 4 6 7 8 9
# 4a
def find_pivot(lst):
    """
    : lst type: list[int] # sorted and then shifted
    : val type: int
    : return type: int (index if found), None (if not found)
    """
    # define pointers at opposite ends of the list
    low = 0
    high = len(lst) - 1

    while low < high:
        mid = (low + high) // 2
        # print('mid', mid , 'mid_val', lst[mid])
        # found pivot
        if lst[mid - 1] > lst[mid] or lst[mid + 1] < lst[mid]:
            return mid + 1
        # pivot is in higher half
        elif lst[low] > lst[mid]: # shifted section is below, search there
            high = mid - 1
        # pivot is in lower half
        else:
            low = mid + 1

    return None
# 4b
def shift_binary_search(lst, target):
    """
    : lst type: list[int] # sorted and then shifted
    : target type: int
    : return type: int (index if found), None (if not found)
    """
    # define pointers at opposite ends of the list
    low = 0
    high = len(lst) - 1
    pivot_index = find_pivot(lst)

    if (target > lst[high]): # target is in the shifted section
        high = pivot_index
    else: # target is in the unshifted section
        low = pivot_index
    
    print('high',high,'low', low)
    
    # normal binary search
    while low < high:
        mid = (low + high) // 2
        # found target
        if lst[mid] == target:
            print('mid', mid , 'mid_val', lst[mid])
            return mid
        # target is in higher half
        elif lst[mid] < target:
            low = mid + 1
        # target is in lower half
        else:
            high = mid - 1
    
    return None

def main():
    # test cases
    print(is_palindrome('racecar'))
    print(is_palindrome('hello'))
    print(is_palindrome(''))
    
    print(reverse_vowels('tandon'))
    print(reverse_vowels('i u a e i e o'))

    print(find_missing([0, 1, 2, 3, 4, 5, 6, 8]))

    print(find_pivot([15, 20, 21, 1, 3, 6, 7, 10, 12, 14]))

    print(shift_binary_search([15, 20, 21, 1, 3, 6, 7, 10, 12, 14], 21))
   

if __name__ == '__main__':
    main()

