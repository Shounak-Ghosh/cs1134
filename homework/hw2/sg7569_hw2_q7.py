def findChange(lst01):
    # define pointers at opposite ends of the list
    low = 0
    high = len(lst01) - 1

    while low < high:
        mid = (low + high) // 2
        if lst01[mid] == 1 and lst01[mid - 1] == 0: # found the change
            return mid
        elif lst01[mid] == 0 and lst01[mid - 1] == 0: # change is higher in the list
            low = mid + 1
        else: # change is lower in the list
            high = mid - 1

def main():
    lst01 = [0, 0, 0, 0, 0,0,0, 1,1, 1, 1]
    print(findChange(lst01))

if __name__ == "__main__":
    main()