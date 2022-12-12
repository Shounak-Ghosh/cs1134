from ChainingHashTableMap import ChainingHashTableMap as map

'''
Vitamins:
1)
a) [ , , , 37, , , ]
b) [47, , , 37, , , ]
c) [47, , , 37 -> 51, , , ]
d) [47, , , 51, , , ]
e) [47, , , 51 -> 65, , ]
f) [47, 104, , 51 -> 65, , , ]
g) [47, 104, , 8, 51 -> 65, , ]
h) [47 -> 5, 104, , 8, 51 -> 65, , ]
i) [47 -> 5, 104, , 8, 51 -> 65, 10, ]
j) [ , , , , , , , 47 -> 5, 104, 7, 8, 51 -> 65, 10, ]
h) [ , , , , , , , 47 -> 5, 104, 7, , 51 -> 65, 10, ]

2) 
The load factor is 2000/25 = 80

3) 
Worst-case runtime is O(n). The function compares
the two strings and returns True if the strings contain
the same characters, and False otherwise.

The outputs of the following are:
print(mystery("cheaters", "teachers")): True
print(mystery("engineering", "gnireenigne")): True
print(mystery("Python", "nohtyp")): False
'''

def most_frequent(lst):
    m = map()

    for i in lst:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    
    max = 0
    max_key = lst[0]
    for key in m:
        if m[key] > max:
            max = m[key]
            max_key = key
    
    return max_key

def most_unique(lst):
    m = map()

    for i in range(len(lst)):
        if lst[i] in m:
            m[lst[i]][0] += 1
        else:
            m[lst[i]] = [1,i]

    # print(m)
    
    unique_key = None
    for key in m:
        if m[key][0] == 1:
            if not unique_key:
                unique_key = key
            elif m[key][1] < m[unique_key][1]:
                unique_key = key
    
    return unique_key

def two_sum(lst, target):
    m = map()

    # key as lst element, value as lst index
    for i in range(len(lst)):
        if lst[i] in m:
            m[lst[i]].append(i)
        else:
            m[lst[i]] = [i]
    
    for key in m:
        if target - key in m:
            if key == target - key:
                if len(m[key]) > 1:
                    return m[key][0], m[key][1]
            else:
                return m[key][0], m[target - key][0]

    return None, None


def main():
    lst = [5,9,2,9,0,5,9,7]
    print(most_frequent(lst))
    print(most_unique(lst))

    lst = [-2, 11, 15, 21, 20, 7]
    print(two_sum(lst, 22))

    lst = [-2, 11, 15, 21, 20, 20]
    print(two_sum(lst, 22))


if __name__ == "__main__":
    main()
