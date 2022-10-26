# return a dictionary with the number of times each letter appears in the string
def appearances(s, low, high):
    if low == high:
        return {s[low]: 1}
    else:
        d = appearances(s, low+1, high)
        if s[low] in d:
            d[s[low]] += 1
        else:
            d[s[low]] = 1
        return d


def main():
    print(appearances('hello', 0, 4))
    print(appearances('hello', 1, 4))
    print(appearances('hello', 2, 4))
    print(appearances('hello', 3, 4))
    print(appearances('hello', 4, 4))


if __name__ == '__main__':
    main()
