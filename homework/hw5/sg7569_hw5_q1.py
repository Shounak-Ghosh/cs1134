from ArrayStack import ArrayStack


def interpreter_postfix_calculator():
    # dictionary for variables, values would be more efficient
    variables = []  # list of tuples (variable name, value)
    inp = input("--> ")
    while inp != "done()":
        exprlst = inp.split(" ")
        # remove empty strings
        exprlst = [x for x in exprlst if x != ""]

        # replace variables with their values
        for i in range(len(exprlst)):
            if exprlst[i].isalpha():  # only alow variables to be alpbabetic strings
                for var in variables:
                    if exprlst[i] == var[0]:
                        exprlst[i] = var[1]
                        break

        # case 1 - assignment
        if len(exprlst) >= 2 and exprlst[1] == "=":
            variables.append(
                (exprlst[0], evaluate_postfix_expression(exprlst[2:])))
            # print("variable", exprlst[0], "set to", exprlst[2])
            print(exprlst[0])
        # case 2 - normal expression evaluation
        else:
            print(evaluate_postfix_expression(exprlst))

        inp = input("--> ")


def evaluate_postfix_expression(exprlst):
    '''
    :param exprlst: a list of characters representing a postfix expression
    returns the result of evaluating the postfix expression
    '''

    s = ArrayStack()
    for i in exprlst:
        if i in "-+*/":  # i is an operator
            val1 = s.pop()
            val2 = s.pop()
            s.push(str(eval(val2 + i + val1)))
        else:  # i is an operand
            s.push(i)

    return s.pop()


def main():
    interpreter_postfix_calculator()


if __name__ == '__main__':
    main()
