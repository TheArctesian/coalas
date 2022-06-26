from sqlite3 import Timestamp


def parse():
    print("sd")

def tokenizeHead(array):
    tempArray = array.replace(" ", "").strip().split(",",)
    print(tempArray)
    return tempArray

def tokenizeValues(line):
    tempArray = line.strip().split(",")
    return tempArray
# TODO: Figure out how this works
def defineArrays(Header):
    myStr = Header
    print("The string is:",myStr)
    myVars = locals()
    myVars[myStr] = []


if __name__ == "__main__":
    with open("../Test/testData.csv") as f:
        Headers = f.readline()
        Headers = tokenizeHead(Headers)
        ra = len(Headers)
        print(ra)
        for word in Headers:
            globals()[word] = []
        

        for line in f:
            a = tokenizeValues(line)
            print(a)
            for value in range(ra):
                globals()[Headers[value]].append(a[value])

        print(globals()[Headers[0]])
        print(Timestamp)