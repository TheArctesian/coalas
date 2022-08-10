import os
import re
import csv
import sys


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
    return line.replace(" ", "").strip().split(",") 

def rmFileEnd(filename):
    return filename.replace(".csv", "")
def importCSV(filename):
    dictName = rmFileEnd(filename)
    globals()[dictName] = {}
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        Columns = tokenizeFirstLine(f.readline())
        for i in Columns: 
            globals()[dictName][i] = []
        try:
            for row in reader:
                for i in range(len(Columns)):
                    globals()[dictName][Columns[i]].append(row[i])
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))         

def fmtColsforPrint(string):
    return f'{col.BOL}{col.UND}{col.P}{string}{col.END}'

def fmtRowsforPrint(string):
    return f'{col.C}{string}{col.END}'

def colNames(file):
    cols = [] 
    for i in file:
        cols.append(i)
    return cols

def splitArtoCSV(arr):
    temp = ""
    for i in arr:
        temp += f"{i},"
    temp = temp[:-1]
    return temp
def pcolNames(file):
    cols = splitArtoCSV(colNames(file))
    print(fmtColsforPrint(cols))

def longestCol(file):
    leng = 0
    for i in file.values():
        tlen = len(i)
        if tlen >= leng:
            leng = tlen
    return leng

def shortestCol(file):
    leng = longestCol(file)
    for i in file.values():
        tlen = len(i)
        if tlen <= leng:
            leng = tlen
    return leng

def rowCSV(file, number):
    row = []
    try: 
        for i in file.values():
            row.append(i[number])
    except IndexError: 
        row.append("")

    return row

def phead(file):
    pcolNames(file) 
    leng = shortestCol(file)
    if leng >= 5: 
        leng = 5
    for i in range(leng): 
        row = rowCSV(file, i)
        row = splitArtoCSV(row)
        print(fmtRowsforPrint(row))

def writeCSV(file, filename): 
    with open(filename, 'w') as f:  
        csvwriter = csv.writer(f)
        csvwriter.writerow(colNames(file))
        for i in range(longestCol(file)):
            row = rowCSV(file, i)            
            csvwriter.writerow(row)


if __name__ == "__main__":
    file = 't.csv'
    importCSV(file)
    phead(t)
    writeCSV(t, 'x.csv')
