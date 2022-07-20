import os
import re
import csv

class col:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    PASS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def importData(filename):
    f = open(filename, "r") # open file 
    
    # Parse and clean Headers
    Head = f.readline() # Read first line (Timestamp,Price,Trade Volume...)
    TokenHeaders = tokenizeHead(Head) # 'Tokenize to array['Timestamp', Price', 'TradeVolume'...]

    # Init headers to empty arrays
    for word in TokenHeaders:
        globals()[word] = []
    
    # This takes a little more explanation but for a better one go here https://www.programiz.com/python-programming/methods/built-in/globals
    """
    the globals method returns all the global var kinda 
    for our purposes this sets the column headers as the name of the variable 
    or makes it so the col headers -> []
    eg if we now
    print(Timestamp) => []
    I hope that makes sense, this is a pretty hacky way of doing it but eh 
    """
    
    # Globalized headers values (will need this for mutating state later on)
    globals()["Headers"] = TokenHeaders
    with open('news.csv', 'r') as p:
        reader = csv.reader(p)
        for row in reader:
            for value in range(len(TokenHeaders)): 
                globals()[TokenHeaders[value]].append(row[value]) 
                """
                This line might look a bit complicated but it is really quite simple
                It takes our globalized var which we init to empty arrays
                    example:
                        Timestamp = []
                And appends the values of that row to the col header name 
                So after this runs if we print timestamp again 
                    print(Timestamp) => ['2019-06-26', '2019-06-27', '2019-06-28', '2019-06-29', '2019-06-30', '2019-07-01', '2019-07-02', '2019-07-03']
                """
        f.close()
        p.close()
    for value in range(len(TokenHeaders)): 
        globals()[TokenHeaders[value]].pop(0)
        


def addRow(rowName):
    cleanRow = rowName.strip().replace(" ","")# cleans the row name in case ppl are stupid
    globals()[cleanRow] = [] # init the name row to an empty array
    Headers.append(cleanRow) # adds the row to global headers

def removeCol(rowName):
    if rowName in Headers:
        Headers.remove(rowName)
        globals()[rowName] = [] # this saves a bit of memory but will cause errors if someone tries to remake it later
    else: 
        raise Exception("Row Header does not exist, check if row exists of printHeaders() to see the name formatted name of the row")
    # This works fine for all purposes but the row values will still be saved in the global state so will might cause performance issues
    # TODO: Clean row from global symbols

def removeRow(index): 
    for head in Headers:
        globals()[head].pop(index)

def createCSV(cols):

    globals()["Headers"] = []

    for col in cols:
        col = col.replace(" ", "") #checks for stupid people
        globals()[col] = []
        globals()["Headers"].append(col)
    

def mergeFile(filename):
    with open(filename, 'r') as f:
        Head = f.readline()
        TokenHeaders = tokenizeHead(Head)
        for word in TokenHeaders:
            globals()[word] = []
            globals()["Headers"].append(word)
        for line in f: # Loops through remaining non header values 
            row = tokenizeLine(line) # tokenized line ['2019-06-26', '11766', '188227336', '399624', '57826748']
            for value in range(len(TokenHeaders)): 
                globals()[TokenHeaders[value]].append(row[value]) 



def sort(col, action):
    try:  
        if action == "acc": # Sort by acceding  
            li = []
            # sorts the array and adds the index of the sorted arrays to the array li
            intedArray = []
            for string in col: 
                intedArray.append(int(string))

            for index in range(len(intedArray)): 
                li.append([intedArray[index],index])
                li.sort()
                sort_index = []
            for index in li:
                sort_index.append(index[1])
            
            for array in Headers:  
                if len(globals()[array]) == len(sort_index):
                    temp = []
                    for index in range(len(sort_index)): 
                        tempIndex = sort_index[index]
                        temp.append(globals()[array][tempIndex])
                    globals()[array] = temp
                else: 
                    raise Exception("Index out of range, the length or your col are not the same and so the whole file can not be sorted")
        if action == "des": # Sort by descending order
            li = []
            # sorts the array and adds the index of the sorted arrays to the array li
            intedArray = []
            for string in col: 
                intedArray.append(int(string))

            for index in range(len(intedArray)): 
                li.append([intedArray[index],index])
                li.sort(reverse=True)
                sort_index = []
            for index in li:
                sort_index.append(index[1])
            
            for array in Headers:  
                if len(globals()[array]) == len(sort_index):
                    temp = []
                    for index in range(len(sort_index)): 
                        tempIndex = sort_index[index]
                        temp.append(globals()[array][tempIndex])
                    globals()[array] = temp
                else: 
                    raise Exception("Index out of range, the length or your col are not the same and so the whole file can not be sorted")
    except:
        raise Exception("Col are not integers")

def printHeaders():
    print(f'{col.BOLD}{col.HEADER}{Headers}{col.ENDC}')

def HeadCSV():
    head = "" # init empty row of headers for formatting
    for word in Headers: 
        h = word + ","
        head += h
    # Will return headers in csv form 
        #  ['Timestamp', 'Price', 'TradeVolume', 'TransactionsVolume', 'HashRate'] => Timestamp,Price,TradeVolume,TransactionsVolume,HashRate,
    head = head[:-1]   # remove the last ',' so that the CSV doesn't have extra line
    return head

def rowCSV(int):
    row = "" # init empty string to store row
    for word in Headers: 
        tempArray = globals()[word] # the array of that col
        # catch Index out of bounds error 
        # Maybe that value dose not have a predefined value so need to replace it with empty ',' 
        try: 
            value = tempArray[int] + ','
            row += value
        except IndexError: 
            row+=','
    row = row[:-1] # remove the last ',' so that the CSV doesn't have extra line
    
    return row


def parseFileName(filename):
   name = re.sub(".*/", "", filename)
   name = name.replace(".csv", "")
   return name

def calLongestCol():
    largest = 0
    for word in Headers: 
        tempArray = globals()[word] # the array of that col
        length = len(tempArray) # get length 
        if length > largest: # check if bigger 
            largest = length
    return largest

def printSmall():
    # This is pretty self explanatory
    head = HeadCSV()
    row1 = rowCSV(1)
    row2 = rowCSV(2)
    row3 = rowCSV(3)
    print(f'{col.BOLD}{col.HEADER}{head}{col.ENDC}')
    print(f'{col.BLUE}{row1}{col.ENDC}')
    print(f'{col.BLUE}{row2}{col.ENDC}')
    print(f'{col.BLUE}{row3}{col.ENDC}')

def printAll():
    # So is this 
    head = HeadCSV()
    print(f'{col.BOLD}{col.HEADER}{head}{col.ENDC}')
    for i in range(calLongestCol()):
        row = rowCSV(i)
        print(f'{col.BLUE}{row}{col.ENDC}')

def writeCSV(filename):
    # And this
    # Have to add the \n (newline) because python
    with open(filename, "w") as file:
        file.write(HeadCSV() + '\n')
        for i in range(calLongestCol()):
            row = rowCSV(i)
            file.write(row + '\n')

def tokenizeHead(string):
    return string.replace(" ", "").strip().split(",") # remove spaces and split by ,

def listDir():
    entries = os.listdir('./')
    for entry in entries:
        print(entry)

def listUpDir():
    entries = os.listdir('../')
    for entry in entries:
        print(entry)


if __name__ == "__main__":
    importData('news.csv')
    sort(Trained,'des')
    printSmall()
    writeCSV('p.csv')