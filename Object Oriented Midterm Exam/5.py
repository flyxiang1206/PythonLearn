money = int(input("請輸入金額:"))

result = ""

result += "1000元"+ str(money//1000) +"張\n"

money = money % 1000

result += "500元"+ str(money//500) +"張\n"

money = money % 500

result += "100元"+ str(money//100) +"張\n"

money = money % 100

result += "50元"+ str(money//50) +"個\n"

money = money % 50

result += "10元"+ str(money//10) +"個\n"

money = money % 10

result += "5元"+ str(money//5) +"個\n"

money = money % 5

result += "1元"+ str(money) +"個\n"

print(result)