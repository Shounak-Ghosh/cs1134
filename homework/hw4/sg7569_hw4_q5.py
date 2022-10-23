def count_lowercase(s,low,high):
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    else:
        if s[low].islower():
            return 1 + count_lowercase(s,low+1,high)
        else:
            return count_lowercase(s,low+1,high)

def is_number_of_lowercase_even(s):
    if count_lowercase(s,0,len(s)-1)%2 == 0:
        return True
    else:
        return False