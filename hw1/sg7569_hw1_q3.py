def sum_of_squares(n):
    ans = 0
    for i in range(1, n+1):
        ans += i**2
    return ans

def sum_of_squares2(n):
    ans = [sum(x**2) for x in range(1, n+1)]
    return ans[0]

def sum_of_odd_squares(n):
    ans = 0
    for i in range(1, n+1, 2):
        ans += i**2
    return ans

def sum_of_odd_squares2(n):
    ans = [sum(x**2) for x in range(1, n+1, 2)]
    return ans[0]