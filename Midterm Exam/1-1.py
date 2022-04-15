from cgitb import reset

width = 13
higth = 7

result = ''

for i in range(0,higth):
    for j in range(0,width):
        if i == 0 or i == higth - 1 or j % 4 == 0:
            result += '*'
        else:
            result += ' '
    result += '\n'

print(result)