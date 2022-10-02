def factors(num):
    higher_divisors = [0] * int(num ** .5)
    index = 0
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            yield i
            if i != num // i: # don't include the square root twice
                higher_divisors[index] = num // i
                index += 1

    for i in range(index - 1, -1, -1): # yield the higher divisors in reverse order
        yield higher_divisors[i]

def main():
    num = 100
    for i in factors(num):
        print(i)

if __name__ == "__main__":
    main()
