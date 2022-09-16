from ast import main
from unicodedata import name


class UnsignedBinaryInteger:
    def __init__(self, num_str):
        self.num_str = num_str
    
    def decimal(self):
        return int(self.num_str,2)
    
    def __lt__(self,other):
        return self.decimal() < other.decimal()
    
    def __gt__(self,other):
        return self.decimal() > other.decimal()
    
    def __eq__(self,other):
        return self.decimal() == other.decimal()
    
    def is_twos_power(self):
        return self.decimal() & (self.decimal() - 1) == 0
    
    def largest_twos_power(self):
        twos_power = "1"
        for i in range(1,len(self.num_str)):
            twos_power += "0"
            
        return UnsignedBinaryInteger(twos_power)

    def __repr__(self):
        return "0b" + self.num_str
    
    def __add__(self,other):
        return UnsignedBinaryInteger(bin(self.decimal() + other.decimal())[2:])

def main():
    bint = UnsignedBinaryInteger("1101")
    print(bint)
    print(bint.is_twos_power())
    print(bint.largest_twos_power().decimal())

if __name__ == '__main__':
    main()

