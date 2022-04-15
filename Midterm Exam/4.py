from cgitb import reset

def MySort(list):
    return sorted(list)

dataList = []

dataList.append(int(input("輸入數字1:")))
dataList.append(int(input("輸入數字2:")))
dataList.append(int(input("輸入數字3:")))

print(MySort(dataList))