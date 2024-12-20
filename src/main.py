from manager import getRoom, setRoomUnit, genNewBill, update

def main():

    genNewBill("dec.json","jan.json")

    this_month = [8400,5000,4500,5000,5000,6300,2500,5500,8200,4000,6000,5000,6300,6700,4000,6800]
    update("jan.json",this_month)
    getRoom("jan.json")
    return 0

if __name__=="__main__":
    main()
