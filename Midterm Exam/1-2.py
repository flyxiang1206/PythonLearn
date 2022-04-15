width = 13
higth = 13

result = ''

for i in range(0,higth):
    for j in range(0,width):
        if i == 0 or i == higth - 1 or j == 0 or j == width - 1 or j == i or j == higth - i - 1:
            result += '＊'
        else:
            result += '　'
    result += '\n'

print(result)