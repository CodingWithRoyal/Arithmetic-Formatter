import re


def arithmetic_arranger(problems):

    resp = ""
    l1 = ""
    l2 = ""
    l3 = ""
    l4 = ""

    for p in problems:
        p = p.split()  # problem
        length = len(max(p))  # length of biggest operand in list

        # There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
        probSpace = length + 1 + 1

        i = 0  # index
        for x in p:
            if i != 1:
                spacesToAdd = probSpace - len(x)
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

            # line 3 - dash
            dashesToAdd = probSpace
            while dashesToAdd > 0:
                l3 += "-"
                dashesToAdd -= 1
            l3 += "    "

            # increase index
            i += 1

    resp = l1 + "\n" + l2 + "\n" + l3
    return resp
