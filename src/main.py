from manager import getRoom, setRoomUnit, genNewBill

def main():

    genNewBill("dec.json","jan.json")
    getRoom("jan.json")

    setRoomUnit("jan.json",1,500)
    getRoom("jan.json")
    return 0

if __name__=="__main__":
    main()
