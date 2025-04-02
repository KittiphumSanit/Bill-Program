from manager import getRoom, genNewBill, update, totalValue, total_Electricity_Value

from billgenerate import create_pdf

def main():

    # this_month = [8408,4864,4461,4776,5039,6189,2374,5330,8263,3937,5950,4861,6188,6484,3842,6458]

    this_month = []
    this_cleaner = []

    newMonth = str(input("Enter new month(short): "))
    oldMonth = str(input("Enter old month(short): "))

    newMonthJSON = newMonth + '.json'
    oldMonthJSON = oldMonth + '.json'
    
    check = int(input("Edit more...(0,1) : "))
    if check == 1:
        for i in range(16):
            e = int(input(f"room {(i+1)}: "))
            this_month.append(e)
            c = int(input(f"room {(i+1)} cleaner(0,1): "))
            this_cleaner.append(c)
    else:
        for i in range(16):
            e = int(input(f"room {(i+1)}: "))
            this_month.append(e)
            this_cleaner.append(0)

    
    
    # create new data from old data
    genNewBill(oldMonthJSON, newMonthJSON, this_cleaner)
    update(newMonthJSON, this_month)
    getRoom(newMonthJSON)
    x = totalValue("newMonthJSON")
    y = total_Electricity_Value("newMonthJSON")

    print(f"Summary = {x-y}")

    # create bill pdf from json file
    create_pdf(newMonthJSON)

    return 0

if __name__=="__main__":
    main()
