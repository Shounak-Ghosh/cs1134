def powers_of_two(n):
    for i in range(n):
        yield 2 ** i

def main():
    for i in powers_of_two(10):
         print(i)

if __name__ == '__main__':
    main()



