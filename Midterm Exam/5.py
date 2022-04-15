width = 9
higth = 9

result = ''

for i in range(higth , 0 , -1):
    for j in range(width , 0 , -1):
        if (i*j)/10 < 1:
            result += ' '
        result += str(i * j)
        result += ' '
    result += '\n'

print(result)