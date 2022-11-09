km = input("請輸入公里數:")
time = input("請輸入上車時間(幾時):")
km = float(km)
time = int(time)

money = 0

if km < 1.5:
    money = 85
else:
    money = 85 + ((km-1.5) / 0.3 ) * 5

if time>=23 or time <= 6:
    money = money * 1.2

print("車資為",money,"元")