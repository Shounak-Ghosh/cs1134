
def reverse_list(lst, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst) -1
    
    for i in range(int((high-low)/2 + 0.5)):
        lst[low+i], lst[high-i] = lst[high-i], lst[low+i]
    return lst

def move_zeros(lst):
    first_empty = 0
    for i in range(len(lst)):
        if lst[i] != 0: # if not zero, move to first empty slot
            lst[first_empty], lst[i] = lst[i], 0
            first_empty += 1
    return lst

# shift list by n places
def shift(lst,k,direction='right'):
    if direction == 'left':
        reverse_list(lst,0,k-1)
        reverse_list(lst,k,len(lst)-1)
        reverse_list(lst)
    elif direction == 'right':
        reverse_list(lst,0,len(lst)-k-1)
        reverse_list(lst,len(lst)-k,len(lst)-1)
        reverse_list(lst)
    return lst

def maximum_sum_subarray(lst,k):
    dist = len(lst) // k
    max_sum = 0
    prev_sum = 0
    for i in range(dist):
        prev_sum += lst[i]
    # print(dist)
    # print('initial max_sum', max_sum)

    for i in range(len(lst) - dist + 1):
        if i + dist >= len(lst):
            return max_sum
        # print("current range", lst[i], lst[i+dist])
        cur_sum = prev_sum - lst[i] + lst[i+dist]
        prev_sum = cur_sum
        # print('current sum', cur_sum)
        max_sum = max(max_sum, cur_sum)

       

def main():
    lst = [1, 2, 3, 4, 5, 6]
    print(reverse_list(lst))
    lst = [1, 2, 3, 4, 5, 6]
    print(reverse_list(lst,low=1,high=3))

    lst = [0, 1, 0, 3, 13, 0]
    print(move_zeros(lst))

    lst = [1, 2, 3, 4, 5, 6]
    print(shift(lst, 2))

    print(maximum_sum_subarray([1,12,-5,-6,50,3],2))
    print(maximum_sum_subarray([-10,7,2],2))

if __name__ == "__main__":
    main()