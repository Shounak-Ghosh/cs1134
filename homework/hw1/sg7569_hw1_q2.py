def shift(lst, k, dir='left'):
    # shifts original list by k positions to the left
    if dir == 'left':
        ans =  lst[k:] + lst[:k]
    elif dir == 'right':
        ans = lst[-k:] + lst[:-k]
    
    for i in range(len(lst)):
            lst[i] = ans[i]
    return lst
        

def main():
    lst = [1, 2, 3, 4, 5, 6]
    print(shift(lst, 2))
    print(shift(lst, 2, 'right'))

if __name__ == '__main__':
    main()
