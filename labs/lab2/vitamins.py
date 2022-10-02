from tkinter import Y


lst = [1,2,3]
def func(lst):
    lst.append(4)
    lst = [5,6,7,8]
    print(lst)
func(lst)
print(lst)
print([i//i for i in range(-3,4) if i != 0])
print("a"*2)

def sum_to(n):
    
    for i in range(1,n+1):
        total = i * (i + 1) // 2
        yield total

for i in sum_to(10):
     print(i, end = ', ')