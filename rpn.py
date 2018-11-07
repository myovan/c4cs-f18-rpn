#!/usr/bin/env python3

import colored
from colored import stylize
def calculate(arg):
    stack = []

    tokens =arg.split()

    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            elif token == '/':
                result = val1 / val2

            stack.append(result)
    if len(stack) > 1:
        raise ValueError("Too many arguments on the stack")
    return(stack[0])


def main():
    while True:
        result = calculate(input('rpn calc> '))
        if result < 0:
            print(stylize(result, colored.fg("green")))
        else:
            angry = colored.fg("red") + colored.attr("bold")
            print(stylize(result, angry, colored.attr("underlined")))

if __name__ == '__main__':
    main()

