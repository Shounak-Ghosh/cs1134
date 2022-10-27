def count_lowercase(s, low, high):
    if len(s) == 0 or low > high:  # edge/base case, empty string or no elements between low and high
        return 0
    if high > len(s) - 1 or low < 0:  # edge case, params are out of bounds
        raise ValueError("parameters out of bounds")
    elif low == high: # base case, only one element between low and high
        if s[low].islower():
            return 1
        else:
            return 0
    else:
        if s[low].islower():
            return 1 + count_lowercase(s, low+1, high)
        else:
            return count_lowercase(s, low+1, high)

# "flip" between T/F for next and curr to keep track if the number of lowercase letters is even
def is_number_of_lowercase_even(s, low, high):
    if len(s) == 0:  # edge case, empty string
        return True
    if high > len(s) - 1 or low < 0:  # edge case, params are out of bounds
        raise ValueError("parameters out of bounds")
    if low > high:  # base case, no elements between low and high
        return None
    next = is_number_of_lowercase_even(s, low+1, high)
    curr = s[low].islower()
    if next is None: # no more characters to check
        return not curr # return False if current (last) character is lowercase
    if curr:  # current character is lowercase
        return not next # have to flip if current character is lowercase
    else:
        return next # keep current value b/c curr is not lower case


def is_number_of_lowercase_even2(s, low, high):
    return count_lowercase(s, low, high) % 2 == 0


def main():
    print("false as int", int(False))
    print()
    print(count_lowercase("aBCCahshs", 0, len("aBCCahshs")-1))
    print(count_lowercase("aBCCahshs", 0, 3))
    print(count_lowercase("ABC", 0, len("ABC")-1))
    print(count_lowercase("A", 0, len("A")-1))

    print("\nOutput", "Expected")
    print(is_number_of_lowercase_even("aBCCahshs", 0, len("aBCCahshs")-1),
          is_number_of_lowercase_even2("aBCCahshs", 0, len("aBCCahshs")-1))
    print()
    print(is_number_of_lowercase_even("aBCCahshs", 0, 3),
          is_number_of_lowercase_even2("aBCCahshs", 0, 3))
    print()
    print(is_number_of_lowercase_even("ABC", 0, len("ABC")-1),
          is_number_of_lowercase_even2("ABC", 0, len("ABC")-1))
    print()
    print(is_number_of_lowercase_even("A", 0, len("A")-1),
          is_number_of_lowercase_even2("A", 0, len("A")-1))

    test_str = ""
    print("\ntest str", test_str, "len", len(test_str))

    print(is_number_of_lowercase_even(test_str, 0, len(test_str)-1),
          is_number_of_lowercase_even2(test_str, 0, len(test_str)-1))


if __name__ == '__main__':
    main()
