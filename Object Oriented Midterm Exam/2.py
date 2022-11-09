def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  

intA = input("請輸入第一個正整數:")
intB = input("請輸入第二個正整數:")
intA = int(intA)
intB = int(intB)

total = 0

for number in range(intA, intB + 1, 1):
    total += factorial(number)

print(total)