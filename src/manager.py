from data import saveDATA, readDATA

def genNewBill(firstFile, secondFile, cleaner):

    firstFileData = readDATA(firstFile)
    saveDATA(firstFileData,secondFile)
    secondFileData = readDATA(secondFile)

    i = 0
    for r in secondFileData.get("Room"):
        r["Before_Month"] = r["This_Month"]
        r["This_Month"] = 0
        r["Unit"] = 0
        r["Electricity_Value"] = 0
        if cleaner[i] == 1:
            r["Out"] = True
        else:
            r["Out"] = False
        r["Debt"] = 0
        i+=1

    saveDATA(secondFileData,secondFile)


def getRoom(fileName):

    data = readDATA(fileName)

    for i in data.get("Room"):
        print(i)
        
    return data.get("Room")

def setRoomUnit(fileName,roomNumber,value):

    data = readDATA(fileName)
    data.get("Room")[roomNumber-1]["This_Month"] = value

    saveDATA(data,fileName)

def update(fileName,value):

    data = readDATA(fileName)

    i = 0
    for r in data.get("Room"):
        r["This_Month"] = value[i]
        r["Unit"] = r["This_Month"] - r["Before_Month"]
        r["Electricity_Value"] = r["Unit"] * data.get("Electricity_Price")
        if r["Out"] == True:
            r["Debt"] = data.get("Cleaner") + r["Electricity_Value"]
        else:
            r["Debt"] = data.get("Rent_Price") + r["Electricity_Value"]
        i += 1

    saveDATA(data,fileName)


def totalValue(fileName):
    data = readDATA(fileName)

    sum = 0

    for r in data.get("Room"):
        sum += r["Debt"]

    print(f"Debt Total = {sum}")
    return sum

def total_Electricity_Value(fileName):
    data = readDATA(fileName)

    sum = 0

    for r in data.get("Room"):
        sum += r["Electricity_Value"]

    print(f"Electricity Value Total = {sum}")
    return sum