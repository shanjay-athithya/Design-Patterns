import re

def binary(given):
    pattern = '^[01]+$'
    if re.match(pattern, given):
        print("The given pattern is binary")
    else:
        print("The given pattern is not binary")

if __name__ == '__main__':
    binary("01010")
    binary("00021")