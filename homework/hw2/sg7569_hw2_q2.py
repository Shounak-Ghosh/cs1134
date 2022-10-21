# O(n) = log(n)
def example3(n):
    i = 1
    sum = 0
    counter = 0
    while i < n * n:
        i *= 2
        sum += i
        counter += 1
    print(counter)
    return sum

# O(n) = n


def example4(n):
    counter = 0
    i = n
    sum = 0
    while i > 1:
        for j in range(i):
            sum += i * j
            counter += 1
        i //= 2
    print(counter)
    return sum


example3(10000)
example4(10000)
