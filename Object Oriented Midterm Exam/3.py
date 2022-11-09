def BubbleSort(data):
    n = len(data)
    while n > 1:
        n-=1
        for i in range(n):        
            if data[i] < data[i+1]:  
                data[i], data[i+1] = data[i+1], data[i]
    return data

data = []

data.append(int(input("請輸入第一個整數:")))
data.append(int(input("請輸入第二個整數:")))
data.append(int(input("請輸入第三個整數:")))
data.append(int(input("請輸入第四個整數:")))

print(BubbleSort(data))