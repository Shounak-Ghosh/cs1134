a  = [10**x for x in range(0, 6)]

b = [sum(range(0,2 * x,2)) for x in range(1,11)]

c = [chr(x) for x in range(ord('a'), ord('z')+1)]

def main():
    print("a) ", a)
    print("b) ", b)
    print("c) ", c)

if __name__ == '__main__':
    main()