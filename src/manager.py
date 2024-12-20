from data import saveDATA, readDATA

def genNewBill(firstFile,secondFile):

    firstFileData = readDATA(firstFile)
    saveDATA(firstFileData,secondFile)
    secondFileData = readDATA(secondFile)

    for r in secondFileData.get("Room"):
        r["Before_Month"] = r["This_Month"]
        r["This_Month"] = 0
        r["Unit"] = 0
        r["Electricity_Value"] = 0
        r["Debt"] = 0

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