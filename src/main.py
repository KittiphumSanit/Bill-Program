from manager import getRoom, genNewBill, update

from billgenerate import create_pdf

def main():

    genNewBill("dec.json","jan.json")

    this_month = [8408,4864,4461,4776,5039,6189,2374,5330,8263,3937,5450,4861,6188,6484,3842,6458]
    update("jan.json",this_month)
    getRoom("jan.json")

    # create bill pdf
    create_pdf('dec.json')

    return 0

if __name__=="__main__":
    main()
