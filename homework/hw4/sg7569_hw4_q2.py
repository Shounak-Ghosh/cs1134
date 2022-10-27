count1 = 0
count2 = 0
count3 = 0


def fun1(n):
    if n == 0:
        return 1
    else:
        part1 = fun1(n-1)
        part2 = fun1(n-1)
        global count1
        count1 += 1
        res = part1 + part2
        return res


def fun2(n):
    if n == 0:
        return 1
    else:
        res = fun2(n//2)
        global count2
        count2 += 1
        res += n
        return res


def fun3(n):
    if n == 0:
        return 1
    else:
        res = fun3(n//2)
        for i in range(1, n+1):
            global count3
            count3 += 1
            res += i
        return res


def main():
    n = 128
    # print(fun1(n))
    # print(count1, "\n")

    print(fun2(n))
    print(count2)

    print(fun3(n))
    print(count3)


if __name__ == '__main__':
    main()
