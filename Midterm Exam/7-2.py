higth = 6

result = ''

for i in range(1,higth+1):
    for j in range(1,i+1):
        result += str(i)
    result += '\n'

print(result)