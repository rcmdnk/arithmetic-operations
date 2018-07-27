#!/usr/bin/env python
""" Arithmetic operations """

from __future__ import print_function
import sys
import argparse

def addition(var):
    return var[0] + var[1]

def subscription(var):
    return

def multiplication(var):
    return

def division(var):
    return

def main():
    if len(sys.argv) == 1:
        print("Usage: operation <operator> [var1 [var2 [var3...]]]")
        sys.exit(0)

    operator = sys.argv[1]
    var = [float(x) for x in sys.argv[2:]]

    operators = {
        # operator_name: [# of arguments, [operator words]]
        "addition": [2, ["+", "add", "addition", "plus"]],
        "subscription": [2, ["-", "sub", "subscription", "minus"]],
        "multiplication": [2, ["*", "x", "mul", "multiplication", "product"]],
        "division": [2, ["/", "div", "division", "quotient"]],
    }

    operator_name = None
    for name in operators:
        if operator in operators[name][1]:
            operator_name = name

    if operator_name is None:
        print("Unknown operator: %s" % operator)
        sys.exit(1)

    if len(var) != operators[operator_name][0]:
        print("Number of variables for operator %s is: %d" %
              (operator, operators[operator_name][0]))
        sys.exit(2)

    print(eval(operator_name + "(var)"))


if __name__ == "__main__":
    main()
