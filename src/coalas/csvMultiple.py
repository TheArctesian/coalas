import os
import re
import csv

class color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class col:
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    P = '\033[95m'
    C = '\033[96m'
    W = '\033[97m'
    END = '\033[0m'
    BOL = '\033[1m'
    UND = '\033[4m'


def tokenizeFirstLine(line):

    return line.replace(" ", "").strip().split(",") # remove spaces and split by ,

def importCSV(filename):
    dictName = filename.replace(".csv", "")
    globals()[dictName] = {}
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        Columns = tokenizeFirstLine(f.readline())

        print(Columns)
        try:
            for row in reader:
             print(row)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))         
        
if __name__ == "__main__":
    importCSV('t.csv')
