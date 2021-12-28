def xnor(a, b):
    return (a or (not b)) and ((not a) or b)


line = input().split()
a = eval(line[0])
b = eval(line[1])
print(xnor(a, b))

