def print_triangle(n):
    if n == 1:
        print("*")
    else:
        print_triangle(n-1)
        print("*"*n)

def print_opposite_triangles(n):
    if n == 1:
        print("*")
        print("*")
    else:
        print("*"*n)
        print_opposite_triangles(n-1)
        print("*"*n)

# TODO: print ruler function
def print_ruler(n):
    pass

def main():
    # print_triangle(4)
    print_opposite_triangles(4)

if __name__ == '__main__':
    main()