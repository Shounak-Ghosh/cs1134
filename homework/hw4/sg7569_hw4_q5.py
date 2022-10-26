def count_lowercase(s, low, high):
    if len(s) == 0 or low > high:  # base case, empty string or no elements between low and high
        return 0
    elif low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    else:
        if s[low].islower():
            return 1 + count_lowercase(s, low+1, high)
        else:
            return count_lowercase(s, low+1, high)


def is_number_of_lowercase_even(s, low, high):
    if len(s) == 0:  # base case, empty string
        return True
    if low > high:  # base case, no elements between low and high
        return None
    next = is_number_of_lowercase_even(s, low+1, high)
    curr = s[low].islower()
    if next is None:
        return not curr
    if curr:  # current character is lowercase
        return not next
    else:
        return next


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
