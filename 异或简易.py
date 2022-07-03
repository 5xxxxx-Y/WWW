word = input("Input word:")
payload = """"""
for i in word:
    if i == "a":
        payload += '("!"^"@")'
    elif i == "b":
        payload += '("!"^"@")'
    elif i == "c":
        payload += '("#"^"@")'
    elif i == "d":
        payload += '("$"^"@")'
    elif i == "e":
        payload += '("%"^"@")'
    elif i == "f":
        payload += '("&"^"@")'
    elif i == "g":
        payload += '''("'"^"@")'''
    elif i == "h":
        payload += '("("^"@")'
    elif i == "i":
        payload += '(")"^"@")'
    elif i == "j":
        payload += '("*"^"@")'
    elif i == "k":
        payload += '("+"^"@")'
    elif i == "l":
        payload += '(","^"@")'
    elif i == "m":
        payload += '("-"^"@")'
    elif i == "n":
        payload += '("."^"@")'
    elif i == "o":
        payload += '("/"^"@")'
    elif i == "p":
        payload += '("/"^"_")'
    elif i == "q":
        payload += '("/"^"^")'
    elif i == "r":
        payload += '("."^"\\")'
    elif i == "s":
        payload += '("-"^"^")'
    elif i == "t":
        payload += '("/"^"[")'
    elif i == "u":
        payload += '("("^"]")'
    elif i == "v":
        payload += '("("^"^")'
    elif i == "w":
        payload += '("("^"_")'
    elif i == "x":
        payload += '("&"^"^")'
    elif i == "y":
        payload += '''("'"^"^")'''
    elif i == "z":
        payload += '("&"^"\\")'
    elif i == "A":
        payload += '("!"^"`")'
    elif i == "B":
        payload += '("<"^"~")'
    elif i == "C":
        payload += '("#"^"`")'
    elif i == "D":
        payload += '("$"^"`")'
    elif i == "E":
        payload += '("%"^"`")'
    elif i == "F":
        payload += '("&"^"`")'
    elif i == "G":
        payload += '(":"^"}")'
    elif i == "H":
        payload += '("("^"`")'
    elif i == "I":
        payload += '(")"^"`")'
    elif i == "J":
        payload += '("*"^"`")'
    elif i == "K":
        payload += '("+"^"`")'
    elif i == "L":
        payload += '(","^"`")'
    elif i == "M":
        payload += '("-"^"`")'
    elif i == "N":
        payload += '("."^"`")'
    elif i == "O":
        payload += '("/"^"`")'
    elif i == "P":
        payload += '("@"^"~")'
    elif i == "Q":
        payload += '("-"^"|")'
    elif i == "R":
        payload += '("."^"|")'
    elif i == "S":
        payload += '("("^"{")'
    elif i == "T":
        payload += '("("^"|")'
    elif i == "U":
        payload += '("("^"}")'
    elif i == "V":
        payload += '("("^"~")'
    elif i == "W":
        payload += '(")"^"~")'
    elif i == "X":
        payload += '("#"^"{")'
    elif i == "Y":
        payload += '("$"^"{")'
    elif i == "Z":
        payload += '("$"^"~")'
    else:
        payload += i
print("payload:\n"+payload)
