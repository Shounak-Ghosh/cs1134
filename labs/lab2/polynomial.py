from hashlib import new


class Polynomial:
    def __init__(self, coeffs=None):
        if coeffs is None:
            self.coeffs = [0]
        elif isinstance(coeffs, int):
            self.coeffs = [coeffs]
        elif isinstance(coeffs, list):
            self.coeffs = coeffs
        else:
            raise TypeError("coeffs must be a list or int")

    def __add__(self, other):
        if isinstance(other, Polynomial):
            if len(self.coeffs) > len(other.coeffs):
                return Polynomial([self.coeffs[i] + other.coeffs[i] for i in range(len(other.coeffs))] + self.coeffs[len(other.coeffs):])
            else:
                return Polynomial([self.coeffs[i] + other.coeffs[i] for i in range(len(self.coeffs))] + other.coeffs[len(self.coeffs):])
        elif isinstance(other, int):
            return Polynomial([self.coeffs[0] + other] + self.coeffs[1:])
        else:
            raise TypeError("other must be a Polynomial or int")

    def __repr__(self):
        if self.coeffs is None:
            return "0"
        elif isinstance(self.coeffs, int):
            return str(self.coeffs)
        elif isinstance(self.coeffs, list):
            return " + ".join([str(self.coeffs[i]) + "x^" + str(i) for i in range(len(self.coeffs)-1, -1, -1)])
        else:
            raise TypeError("coeffs must be a list or int")
    
    def __call__(self, x):
        return sum([self.coeffs[i] * x**i for i in range(len(self.coeffs))])

def main():
    p1 = Polynomial([3, 7, 0, -9, 2])
    p2 = Polynomial([2, 0, 0, 5, 0, 0, 3])
    p3 = p1 + p2
    print(p1)
    print(p2)
    print(p3.coeffs)
    print(p1(1)) # return 3 
    print(p2(1)) # return 10 
    print(p3(1)) # return 13


if __name__ == '__main__':
    main()
