import csv

def importData(filename):
    f = open(filename, "r") # open file 
    
    # Parse and clean Headers
    Headers = f.readline() # Read first line (Timestamp,Price,Trade Volume...)
    TokenHeaders = tokenizeHead(Headers) # 'Tokenize to array['Timestamp', Price', 'TradeVolume'...]

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
    
    # Now we append the values of each line to the array 

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
    f.close

def tokenizeHead(string):
    return string.replace(" ", "").strip().split(",")

def tokenizeLine(string):
    return string.strip().split(",")
if __name__ == "__main__":
    importData("../Test/testData.csv")
    print(Price)