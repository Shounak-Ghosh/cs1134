from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue


def permutations(lst):
    not_used = ArrayStack()  # stack of items not used yet
    perms = ArrayQueue()  # queue of permutations

    for i in lst:  # add all lst items to stack
        not_used.push(i)

    perms.enqueue([])  # start with empty list
    while not not_used.is_empty():
        item = not_used.pop()  # element to be inserted
        # for each current permutation, insert item into every possible position
        for i in range(len(perms)):
            perm = perms.dequeue()
            for j in range(len(perm)+1):
                perms.enqueue(perm[:j] + [item] + perm[j:])

    ans = []

    while not perms.is_empty():
        ans.append(perms.dequeue())

    return ans


def main():
    print(permutations([1, 2, 3]))


if __name__ == '__main__':
    main()
