import csv
import string


def parse():
    print("sd")

def tokenizeHead(array):
    tempArray = array.replace(" ", "").strip().split(",")
    return tempArray

def tokenizeValues(line):
    tempArray = line.strip().split(",") 
    # If CSV file is 
    """
    Date,Fizz,Buzz
    04-20-2020,Monty,Python
    """
    # Will parse to 
    return tempArray

def getLenHeaders():
    return len(TokenHeaders)
    
def importData(filename):
    f = open(filename, "r") # open file 
    ColHeaders = f.readline() # Read first line 
    TokenHeaders = tokenizeHead(ColHeaders) # Split Col See tokenize
    print(TokenHeaders)
    for word in TokenHeaders:
        globals()[word] = []
        
    
    for line in f:
        a = tokenizeValues(line)
        print(a)
        for value in range(len(TokenHeaders)):
            globals()[f'{TokenHeaders}{value}'].append(a[value])
    globals().update(locals())
    f.close()

def addRow(row):
    globals()[row] = []
    TokenHeaders.append(row)

def removeRow(row):
    if row in TokenHeaders:
        TokenHeaders.remove(row)
    else:
        raise Exception("Row header does not exist")

def getRowMax():
    max = 0
    len = getLenHeaders()
    for word in TokenHeaders:
        for num in range(len):
            tempLen = len(globals()[f'{word}{num}'])
            if tempLen > max:
                max = tempLen
    return max

def writeData(filename):
    file = open(filename, "w")
    writer = csv.writer(file)
    tempTH = TokenHeaders # this is just in case people are stupid which if we site are fav man Thomas Bays they are
    tempH = ""
    for text in tempTH:
        CHead = text + ","
        tempH += CHead
    print(tempH)
    file.write(tempH)
    rowMax = getRowMax()
    print(f"rowMax = {rowMax}")
    headCount = getLenHeaders()
    for number in range(rowMax):
        globals()['row%s' % number] = []
    
    for head in range(headCount):
        for number in range(rowMax):
           temp = globals()[tempTH[head]] 
           globals()[f"row{number}"] += temp
    
    for row in range(rowMax):
        with open(filename, "a") as f:
            temp = ""
            ",".join(globals()[f"row{row}"])
            print(temp)
            f.write(temp)
    

    file.close()
    f.close()
    

if __name__ == "__main__":
    importData("../Test/testData.csv")
    print(globals()[TokenHeaders[0]])

    globals()[TokenHeaders[0]].append("This is a test value")

    print(Timestamp)

    #writeData("s.csv")
