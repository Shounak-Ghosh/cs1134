def sum_to(n):
    if n == 1:
        return 1
    else: # goes down from n to 1
        return n + sum_to(n-1)

def product_evens(n):
    if n == 0:
        return 1
    else: # assumes n is even
        return n * product_evens(n-2)

def find_max(lst,low,high):
    if low == high: # base case, only one element between low, high
        return lst[low]
    else:
        max = find_max(lst,low+1,high) # recursive call, increment low by 1
        if lst[low] > max: # if current element is greater than max, return it
            return lst[low]
        else:
            return max

def is_palindrome(s):
    if len(s) <= 1: # base case, empty string or single character
        return True
    else:
        if s[0] == s[-1]: # if first and last characters are equal
            return is_palindrome(s[1:-1]) # recursive call, remove first and last characters
        else:
            return False

def binary_search(lst, low, high, val):
    if low > high: # base case, val not found
        return -1
    else:
        mid = (low + high) // 2
        if lst[mid] == val: # val found
            return mid
        elif lst[mid] > val: # mid is too high, search lower half
            return binary_search(lst, low, mid-1, val)
        else: # mid is too low, search upper half
            return binary_search(lst, mid+1, high, val)

# goofy ah method
def vc_count(word, low, high):
    if low > high: # base case, no more characters
        return (0,0)
    else:
        if word.lower()[low] in 'aeiou': # if character is a vowel
            return (1 + vc_count(word, low+1, high)[0], vc_count(word, low+1, high)[1])
        else:
            return (vc_count(word, low+1, high)[0], 1 + vc_count(word, low+1, high)[1])

# TODO: recursive sum triangle of the elements of lst
def list_sum_triangle(lst):
    pass

def main():
    print(sum_to(5))
    print(product_evens(8))
    print(find_max([1,2,3,4,5],0,3))
    print(is_palindrome('racecar'))
    print(is_palindrome('hello'))
    print(binary_search([1,2,3,4,5],0,4,3))
    print(binary_search([1,2,3,4,5],0,4,6))
    
    word = "NYUTandonEngineering"
    print(vc_count(word,0,len(word)-1))

if __name__ == '__main__':
    main()
