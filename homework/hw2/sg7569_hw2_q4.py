def e_approx(n):
    e = 0
    factorial = 1
    for i in range(n):
        e += 1 / factorial
        factorial *= i + 1

    return e

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx) 
        print("n =", n, "Approximation:", approx_str)

if __name__ == "__main__":
    main()

