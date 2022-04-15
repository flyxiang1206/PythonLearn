from cgitb import reset

higth = 6

result = ''

for i in range(higth,0,-1):
    for j in range(i,higth+1):
        result += str(i)
    result += '\n'

print(result)