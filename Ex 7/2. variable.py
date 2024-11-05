import re

def variable_check(variable):
    check_string = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    check = re.compile(check_string)
    return bool(check.match(variable))

if __name__ == '__main__':
    print(variable_check("Partial_Sum1")) 
    print(variable_check("1Partial"))
