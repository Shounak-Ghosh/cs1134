def revPrint(lst, low, high):
    if low >= high:
        print(lst)
        return
    lst[low], lst[high] = lst[high], lst[low]
    revPrint(lst, low+1, high-1)

def function2(lst):
    if len(lst) == 1:
        lst[0] = 0
        return 1
    return  1 + function2(lst[:len(lst)//2])

def harmonic(n):
    for i in range(1,n+1):
        yield 1/i

def main():
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # revPrint(lst, 0, len(lst)-1)

    # b = [3,1,6,2]
    # print(function2(b))
    # print(b)

    # iters = 4
    # display_list = list(harmonic(iters))
    # print(display_list)

    l = [1] * 10000
    print(function2(l))

if __name__ == '__main__':
    main()
