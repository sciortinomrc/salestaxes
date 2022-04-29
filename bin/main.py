from Pos import Pos
from inputs import inputs

if __name__ == "__main__":
    
    for input in inputs:
        pos = Pos()
        bill = pos.process_basket(input)
        print(bill)
        print("---------------------------")