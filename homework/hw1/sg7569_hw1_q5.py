def fibs(n):
    f0 = 1
    f1 = 1

    if n == 1:
        yield f0
    else:
        yield f0
        yield f1
        while n > 2:
            f2 = f0 + f1
            yield f2
            f0 = f1
            f1 = f2
            n -= 1


def main():
    for curr in fibs(8):
        print(curr)


if __name__ == '__main__':
    main()
