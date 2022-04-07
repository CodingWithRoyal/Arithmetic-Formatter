import re

def arithmetic_arranger(problems, solveIt=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    resp = ""
    l1 = ""
    l2 = ""
    l3 = ""
    l4 = ""

    for prob in problems:
        p = prob.split()  # problem
        try:
            p[0] = int(p[0])
            p[2] = int(p[2])
        except Exception:
            return "Error: Numbers must only contain digits."
        try:
            p[1] = str(p[1])
        except Exception:
            return "Error: Operator must be '+' or '-'."
        
        # largest operand
        lOperand = p[2]
        if p[0] > p[2]:
            lOperand = p[0]
        length = len( str(lOperand) )  # length of biggest operand in list

        if length > 4:
            return "Error: Numbers cannot be more than four digits."

        # There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
        probSpace = length + 1 + 1

        # line 1
        # line 2
        i = 0  # index
        for x in p:
            x = str(x)
            if i != 1:
                spacesToAdd = probSpace - len( x )
                if i == 2:
                    spacesToAdd -= 1

                # make it right align
                while spacesToAdd > 0:
                    x = ' '+x
                    spacesToAdd -= 1

            # save x in lines
            if i == 0:
                l1 += x + "    "
            else:
                # prepend operator in 2nd line
                if i == 1:
                    l2 += x
                else:
                    l2 += x + "    "

            # increase index
            i += 1

        # line 3 - dash
        dashesToAdd = probSpace
        while dashesToAdd > 0:
            l3 += "-"
            dashesToAdd -= 1
        l3 += "    "

        # line 4 - result
        x = p[0]
        y = p[2]
        operator = p[1]

        if operator == "+":
            result = x+y
        elif operator == "-":
            result = x-y
        else:
            return "Error: Operator must be '+' or '-'."
        
        result = str( result )
        spacesToAdd = probSpace - len(result)
        # make it right align
        while spacesToAdd > 0:
            result = ' '+result
            spacesToAdd -= 1
        l4 += result+"    "

    l1 = l1.rstrip()
    l2 = l2.rstrip()
    l3 = l3.rstrip()
    l4 = l4.rstrip()

    if solveIt == True:
        resp = l1 + "\n" + l2 + "\n" + l3 + "\n" + l4
    else:
        resp = l1 + "\n" + l2 + "\n" + l3

    return resp
