# ---------------------------------
# 我最一開始寫的答案
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

# ---------------------------------
# 女友課堂老師說可以的答案

width = 13
higth = 13

result = ''

for i in range(0,higth):
    if i % 2 == 1:
        result += '\n'
    else:
        for j in range(0,width):
            if i == 0 or i == higth - 1 or j % 4 == 0:
                result += '*'
            else:
                result += ' '
        result += '\n'

print(result)

# ---------------------------------
# 我最後覺得最好看的答案

width = 13
higth = 13

result = ''

for i in range(0,higth):
    if i % 2 == 1:
        result += '\n'
    else:
        for j in range(0,width):
            if i == 0 or i == higth - 1 or j % 4 == 0:
                result += '＊'
            else:
                result += '　'
        result += '\n'

print(result)

# ---------------------------------
# 結論 莫名其妙