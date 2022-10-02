def sum_of_squares(n):
    ans = 0
    for i in range(1, n+1):
        ans += i**2
    return ans

def sum_of_squares2(n):
    return sum([x**2 for x in range(1, n+1)])

def sum_of_odd_squares(n):
    ans = 0
    for i in range(1, n+1, 2):
        ans += i**2
    return ans

def sum_of_odd_squares2(n):
    return sum([x**2 for x in range(1, n+1, 2)])

def main():
    print(sum_of_squares(10))
    print(sum_of_squares2(10))
    print(sum_of_odd_squares(10))
    print(sum_of_odd_squares2(10))

if __name__ == '__main__':
    main()