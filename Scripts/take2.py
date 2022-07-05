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
    for line in f: # Loops through remaining non header values 
        row = tokenizeLine(line) # tokenized line ['2019-06-26', '11766', '188227336', '399624', '57826748']
        for value in range(len(TokenHeaders)): 
            globals()[TokenHeaders[value]].append(row[value]) 
            # This line might look a bit complicated but it is really quite simple
            # It takes our globalized var which we init to empty arrays
                # eg Timestamp = []
            # And appends the values of that row to the col header name 
            # So after this runs if we print timestamp again 
                # print(Timestamp) => ['2019-06-26', '2019-06-27', '2019-06-28', '2019-06-29', '2019-06-30', '2019-07-01', '2019-07-02', '2019-07-03']
    f.close()

def addRow(rowName):
    cleanRow = rowName.strip().replace(" ","")# cleans the row name in case ppl are stupid
    globals()[cleanRow] = [] # init the name row to an empty array
    Headers.append(cleanRow) # adds the row to global headers

def removeRow(rowName):
    if rowName in Headers:
        Headers.remove(rowName)
    else: 
        raise Exception("Row Header does not exist, check if row exists of printHeaders() to see the name formatted name of the row")
    # This works fine for all purposes but the row values will still be saved in the global state so will might cause performance issues
    # TODO: Clean row from global symbols

def printHeaders():
    print(f'{col.BOLD}{col.HEADER}{Headers}{col.ENDC}')

def printSmall():
    head = "" # init empty row of headers for formatting
    for word in Headers: 
        h = word + ","
        head += h
    # Will return headers in csv form 
        #  ['Timestamp', 'Price', 'TradeVolume', 'TransactionsVolume', 'HashRate'] => Timestamp,Price,TradeVolume,TransactionsVolume,HashRate,
    row1 = ""
    row2 = ""
    for word in Headers: 
        tempArray = globals()[word]
        value = tempArray[1] + ','
        row1 += value
    for word in Headers: 
        tempArray = globals()[word]
        value = tempArray[2] + ','
        row2 += value
    print(f'{col.BOLD}{col.HEADER}{head}{col.ENDC}')
    print(f'{col.BLUE}{row1}{col.ENDC}')
    print(f'{col.BLUE}{row2}{col.ENDC}')

def tokenizeHead(string):
    return string.replace(" ", "").strip().split(",")

def tokenizeLine(string):
    return string.strip().split(",")
if __name__ == "__main__":
    importData("../Test/testData.csv")
    printHeaders()
    printSmall()