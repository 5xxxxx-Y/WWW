#朋友给的，也不知道最早是哪个师傅写的
def encode(command):
    code = "~`!@#$%&*()-=+_[]{};:<>,.?/|"
    result_1 = ""
    result_2 = ""
 
    for x in command:
        if not command.isalpha():
            result_1 += x
            result_2 += x
        for y in code:
            if chr(ord(x) ^ ord(y)) in code:
                result_1 += y
                result_2 += chr(ord(x) ^ ord(y))
                break
    return f'("{result_1}" ^ "{result_2}")' 
 
a=encode('ls')
print(a)