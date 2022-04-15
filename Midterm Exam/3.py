from cgitb import reset

def CheckIsLeapYear(input):
    if(i%4==0 and i%100!=0) or i%400 ==0:
        return True
    else:
        return False

inputA = int(input("輸入起始年分:"))
inputB = int(input("輸入結尾年分:"))

resultList = []

for i in range(inputA,inputB):
    if CheckIsLeapYear(i):
        resultList.append(i)

print("閏年總數: ")
print(len(resultList))
print("\n閏年包含:\n")

for idx, data in enumerate(resultList):
    print(data)
