
def cription(password, value):
    cript_pass = ''
    for cha in password:
        cript = chr(ord(cha) + value)
        cript_pass += cript    
    return cript_pass

def encryption(readname, writename):
    with open(readname, "r") as infile:
        with open(writename, "w") as outfile:
            for line in infile:
                username, password = line.strip().split()
                encrypted_pass = cription(password, 3)
                outfile.write(f"{username} {encrypted_pass}\n")  # Corrected the newline character

def decryption(readname, writename):
    with open(readname, "r") as infile:
        with open(writename, "w") as outfile:
            for line in infile:
                username, password = line.strip().split()
                decrypted_pass = cription(password, -3)
                outfile.write(f"{username} {decrypted_pass}\n")  # Reverts to the original password

def correctness(original, constructed):
    with open(original, "r") as file1:
        with open(constructed, "r") as file2:
            encrypted_lines = file1.readlines()
            constructed_lines = file2.readlines()
            original_lines = sum(1 for a, b in zip(encrypted_lines, constructed_lines) if a == b)
            total_lines = len(encrypted_lines)  # Use the length of encrypted_lines
            correct_percent = (original_lines / total_lines) * 100
            return f"the percentage of corrected words is : {correct_percent}"

if __name__ == '__main__':
    encryption(r"D:\PYTHON Code\SEM 3\Ex 6\plain.txt",r"D:\PYTHON Code\SEM 3\Ex 6\cript.txt")
    decryption(r"D:\PYTHON Code\SEM 3\Ex 6\cript.txt", r"D:\PYTHON Code\SEM 3\Ex 6\constructed.txt")
    print(correctness(r"D:\PYTHON Code\SEM 3\Ex 6\plain.txt", r"D:\PYTHON Code\SEM 3\Ex 6\constructed.txt"))