import ArrayQueue as aq

def flatten_list_by_depth(lst):
    q = aq.ArrayQueue()
    new_lst = []

    for item in lst:
        q.enqueue(item)
    
    while not q.is_empty():
        item = q.dequeue()
        if type(item) == list:
            for i in item:
                q.enqueue(i)
        else:
            new_lst.append(item)
    
    return new_lst # result is ordered by depth

def main():
    lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
    print(flatten_list_by_depth(lst))

if __name__ == "__main__":
    main()