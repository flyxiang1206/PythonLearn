def CheckIsMultiple(inputA,inputB):
    if inputB % inputA == 0:
        return True
    else:
        return False

inputA = int(input("輸入整數:"))

resultList = []

for i in range(1,101):
    if CheckIsMultiple(inputA,i):
        resultList.append(i)

result = 0

for idx, data in enumerate(resultList):
    result += data

print(result)
