def print_triangle(n):  # n is a positive integer
    if n == 1:
        print("*")
    else:
        print_triangle(n-1)
        print("*"*n)


def print_opposite_triangles(n):  # n is a positive integer
    if n == 1:
        print("*")
        print("*")
    else:
        print("*"*n)
        print_opposite_triangles(n-1)
        print("*"*n)


def print_ruler(n):  # n is a positive integer
    if n == 1:
        print("-")
    else:
        print_ruler(n-1)
        print("-"*n)
        print_ruler(n-1)


def main():
    print_triangle(4)
    print()
    print_opposite_triangles(4)
    print()
    print_ruler(4)


if __name__ == '__main__':
    main()
