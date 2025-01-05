from manager import getRoom, genNewBill, update

from billgenerate import create_pdf

def main():

    # this_month = [8408,4864,4461,4776,5039,6189,2374,5330,8263,3937,5950,4861,6188,6484,3842,6458]

    this_month = []

    newMonth = str(input("Enter new month(short): "))
    oldMonth = str(input("Enter old month(short): "))

    newMonthJSON = newMonth + '.json'
    oldMonthJSON = oldMonth + '.json'
    
    for i in range(16):
        e = int(input(f"room {(i+1)}: "))
        this_month.append(e)
    
    
    # create new data from old data
    genNewBill(oldMonthJSON,newMonthJSON)
    update(newMonthJSON,this_month)
    getRoom(newMonthJSON)

    # create bill pdf from json file
    create_pdf(newMonthJSON)

    return 0

if __name__=="__main__":
    main()
