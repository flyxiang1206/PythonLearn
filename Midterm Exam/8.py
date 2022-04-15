from cgitb import reset

sales = int(input("\n銷售金額輸入:"))

basicSalary = 23999

commission = 0

if(sales <= 5000):
    commission = 0.1
elif(5001 <= sales and sales <= 10000):
    commission = 0.13
elif(10001 <= sales and sales <= 15000):
    commission = 0.16
else:
    commission = 0.2

total = round(basicSalary + basicSalary * commission)

print("薪水總額為:")
print("{basicSalary} + {basicSalary}*{commission} = {total}\n"
    .format(
        basicSalary = basicSalary,
        commission = commission,
        total = total
    )
)
