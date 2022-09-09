import random

def can_construct(word, letters):
    """
    word - type: str
    letters - type: str
    return - type: bool
    """
    
    for letter in word:
        if letter not in letters:
            return False
        else:
            letters = letters.replace(letter, "", 1)
    return True

print(can_construct("apples", "aples"))
print(can_construct("apples", "aplespl"))

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __iadd__(self, other):
        self.a += other.a
        self.b += other.b
        return self


    def __repr__(self) :#-> str:
        return f"{self.a} + {self.b}i"
#constructor, output
cplx1 = Complex(5, 2) 
print(cplx1) #5 + 2i

cplx2 = Complex(3, 3) 
print(cplx2) #3 + 3i

#addition
print(cplx1 + cplx2) #8 + 5i

#subtraction
print(cplx1 - cplx2) #2 - 1i

#multiplication First Outer Inner Last 
# cplx1 * cplx2
# (5 + 2i)(3 + 3i) -> multiply (5*3) + (5*3i) + (2i*3) + (2i*3i)
# = 15 + 15i + 6i + 6(i^2) -> simplify = 15 + 21i + 6(-1)
# = 9 + 21i
cpl3 = cplx1 * cplx2
print(cpl3) #9 + 21i
print(cpl3 * cplx1)
#5 + 2i * 9 +21i





#original objects remain unchanged 
print(cplx1) #5 + 2i 
print(cplx2) #3 + 3i

def create_permutation(n):
    """
    n - type: int
    return - type: list
    """
    permutation = [-1] * n
    for i in range(n):
        while True:
            rand = random.randint(0, n-1)
            if rand not in permutation:
                permutation[i] = rand
                break
    return permutation

print(create_permutation(6))
print(create_permutation(9))

def scramble_word(word):
    """
    word - type: str
    return - type: str
    """
    scrambled = ""
    permutation = create_permutation(len(word))
    for i in range(len(word)):
        scrambled += word[permutation[i]]
    return scrambled

print(scramble_word("pokemon"))
print(scramble_word("pokemon"))

def guessing_game(word):
    """
    word - type: str
    return - type: None
    """
    scrambled = scramble_word(word)
    tries = 0
    print("\nUnscramble the word:", " ".join(scrambled))
    while tries < 3:
        guess = input("Try #{}: ".format(tries+1))
        if guess == word:
            print("Yay you got it!")
            break
        else:
            tries += 1
            print("Wrong!")

guessing_game("pokemon")

def add_binary(bin_num1, bin_num2):
    """
    a - type: str
    b - type: str
    return - type: str
    """
    return bin(int(bin_num1, 2) + int(bin_num2, 2))[2:]

print(add_binary("1000", "101")) #1000