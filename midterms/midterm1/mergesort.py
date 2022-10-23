def merge_sort(lst):
    if (len(lst) == 0):
        return
    elif (len(lst) == 1):
        return
    else:
        mid = (0 + len(lst)-1) // 2
        left_lst = lst[ : mid+1]
        right_lst = lst[mid+1 : ]
        merge_sort(left_lst)
        merge_sort(right_lst)
        merged = merge(left_lst, right_lst)
        lst[:] = merged [ : ] # shallow copies of merged assigned to lst?

def merge(srt_lst1, srt_lst2):
    merged_list = []
    i1 = 0
    i2 = 0
    while ((i1 < len(srt_lst1)) and (i2 < len(srt_lst2))): # both pointers are in bounds
        if (srt_lst1[i1] < srt_lst2[i2]):
            merged_list.append(srt_lst1[i1])
            i1 += 1
        else:
            merged_list.append(srt_lst2[i2])
            i2 += 1
    # in the case lst1 is longer than lst2
    while (i1 < len(srt_lst1)):
        merged_list.append(srt_lst1[i1])
        i1 += 1
    # in the case lst2 is longer than lst1
    while (i2 < len(srt_lst2)):
        merged_list.append(srt_lst2[i2])
        i2 += 1
    return merged_list

def main():
    lst = [1, 7, 2, 6, 3, 5, 4]
    merge_sort(lst)
    print(lst)

if __name__ == '__main__':
    main()
