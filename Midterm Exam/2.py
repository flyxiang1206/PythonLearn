def CheckIsPrimeNumber(input):
    c = 2
    while c < input:
        if input % c == 0:
            return False
        c += 1
    if c == input:
        return True

inputA = int(input("輸入起始數值:"))
inputB = int(input("輸入起始數值:"))

resultList = []

for i in range(inputA,inputB):
    if(CheckIsPrimeNumber(i)):
        resultList.append(i)

result = 0

for idx, data in enumerate(resultList):
    result += data

print(result)