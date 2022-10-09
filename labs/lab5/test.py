import ArrayList


def main():
    a = ArrayList.ArrayList()
    a.extend([1, 2, 3])
    print(a)
    print(a[-3])

    b = ArrayList.ArrayList()
    b.extend([4, 5, 6])
    print(a + b)

    print(a * 2)
    print(2 * a)

    c = ArrayList.ArrayList('python')
    print(c)

    c = ArrayList.ArrayList(range(10))
    print(c, c.n)
    
    c.remove(5)
    print(c, c.n)

    d = ArrayList.ArrayList([1,2,3,2,3,4,2,2])
    d.removeAll(2)
    print(d, d.n)
  


    ls = [4, 5, 6]
    print(ls[-1])

if __name__ == '__main__':
    main()