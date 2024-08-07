#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    from sys import argv, exit

    args = len(argv) - 1

    if args != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])

        if argv[2] == '+':
            print('{} + {} = {}'.format(a, b, add(a, b)))
        elif argv[2] == '-':
            print('{} - {} = {}'.format(a, b, sub(a, b)))
        elif argv[2] == '*':
            print('{} * {} = {}'.format(a, b, mul(a, b)))
        elif argv[2] == '/':
            print('{} / {} = {}'.format(a, b, div(a, b)))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
