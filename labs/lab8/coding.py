from ArrayStack import *


def stack_sum(s):
    if len(s) == 1:
        return s.top()
    else:
        return s.pop() + stack_sum(s)


def eval_prefix(exp_str):
    exp_lst = exp_str.split(" ")
    s = ArrayStack()

    # evaluate prefix expression
    for i in range(len(exp_lst)-1, -1, -1):
        if exp_lst[i].isdigit():
            s.push(exp_lst[i])
        elif exp_lst[i] in "+-*/":
            s.push(eval(str(s.pop()) + exp_lst[i] + str(s.pop())))

    return s.pop()


def flatten_list(lst):
    s = ArrayStack()
    ret_lst = []

    # push all elements of lst onto stack
    for i in range(len(lst)-1, -1, -1):
        s.push(lst[i])

    while not s.is_empty():
        # print(s.data)
        if type(s.top()) == list:
            curr_lst = s.pop()
            for i in range(len(curr_lst)-1, -1, -1):
                s.push(curr_lst[i])  # s.top() is a list
        else:
            ret_lst.append(s.pop())

    return ret_lst


def main():
    s = ArrayStack()
    s.push(1)
    s.push(-14)
    s.push(5)
    s.push(6)
    s.push(-7)
    s.push(9)
    s.push(10)
    s.push(-5)
    s.push(-8)

    print(stack_sum(s))

    print(eval_prefix("- + * 16 5 * 8 4 20"))

    lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]

    print(flatten_list(lst))



if __name__ == "__main__":
    main()
