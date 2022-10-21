def factors(num):
    for i in range(1, int(num ** .5)):
        if num % i == 0:
            yield i
    for i in range(int(num ** .5), 0, -1):
        if num % i == 0:
            yield num // i


def main():
    num = 100
    for i in factors(num):
        print(i)


if __name__ == "__main__":
    main()
