def PrintPic(count):
    printString = ""

    for _ in range(0,count,1):
        printString += "Ｏ"
    printString += "\n"

    
    for i in range(0, (count-3) // 2 ,1):
        for j in range(0, count ,1):
            if j == 0 or j == count - 1:
                printString += "Ｏ"
            elif j == count // 2:
                printString += "　"
            else:
                printString += "ｘ"
        printString += "\n"
    
    for j in range(0, count ,1):
        if j == 0 or j == count - 1:
            printString += "Ｏ"
        else:
            printString += "　"
    printString += "\n"

    for i in range(0, (count-3) // 2 ,1):
        for j in range(0, count ,1):
            if j == 0 or j == count - 1:
                printString += "Ｏ"
            elif j == count // 2:
                printString += "　"
            else:
                printString += "ｘ"
        printString += "\n"
    
    for _ in range(0,count,1):
        printString += "Ｏ"
    printString += "\n"
    
    print(printString)
    return

while(True):
    count = int(input("請輸入一個奇數:"))
    if count % 2 == 1:
        PrintPic(count)
        break
    else:
        print("A")