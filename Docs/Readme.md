# Use

If you have used R before this will feel pretty familiar but the whole thing at least to be feels like the rational way of doing things

## Core Functions

### Import Data

To import your file use the function

```py
importData(filename)
```

This will bring all the data from your CSV and init them to arrays with that are named after your headers.

Example:
If I have a csv file like this:

```csv
timestamp,name of user,action
20-04-2020,the arctesian,sleep
20-04-2069,daniel,deaded
```

after importing the data you will get 3 arrays of

```py
timestamp = '20-04-2020', '20-04-69'
nameofuser = 'the arctesian', 'daniel'
action = 'sleep', 'deaded'
```

### Create CSV

If you don't have a csv file already you can you the create CSV function to make a new CSV

To do so pass in an array of strings for you col names

```py
colNames = ["foo", "bar", "biz"]
createCSV(colNames)
```

then adding some values to array and writing like

```py
foo.append("james")
bar.append("lars")
biz.append("kirk")
writeCSV("s.csv")
```

Will output a CSV file of

```cs
foo,bar,biz
james,lars,kirk
```

### Write to file

Writes the current state of your arrays to a file

Pass the file name relative to where you run the file you can get your dir but calling the function

```

listDir()

```

Which will print the current files in your dir

```

listUpDir()

```

Will list the ../ dir or the previous directory. I am writing this on arch btw so I have no clue if this will work on non unix systems. If you are running windows you deserve it anyways.

To write just call

```py
writeCSV("yourFileName.csv")
```

## Row manipulation

### addCol

To add a row to your CSV file pass a string of the name of your row to the addRow function

```py
addCol(newRow)
```

this will add the row to the your headers and init a new array with your row name

```py
newCol = []
```

**Warning**

if you pass a rowName like `' Tokenized Values '` this string will be parsed into `'TokenizedValues'`. and to mutate the state of it you will need to use the new parsed value.

### remove Col

This function checks if the colName is in the headers and removes it

to call it pass the colName in string format into the function

```py
removeCol('rowName')
```

The same as before please use printHeaders() to check the appropriate col name

### remove Row

Quite self explanatory it removes row at index `x` with the index starting at 0 like normal arrays

```
removeRow(0)
```

### Sort

This function allows you to sort the entire CSV by one row

The function takes in col name and a action either `"acc"` for accenting sort or `"des"` for descending sort

- Example (using testData.csv)

```py
sort(Price, 'acc')
```

=>

```cs
Timestamp,Price,TradeVolume,TransactionsVolume,HashRate
2019-07-02,10579,171482109,373409,59910359
2019-07-01,10738,172764922,336862,61165896
2019-07-03,10805,240430091,397554,61131189
```

### Merge File

This function merges two CSV files together and is currently the only method to work with 2 different CSV files

```py
mergeFile('path to file')
```

### mutating rows

For changing the values just used the standard python array manipulation functions, if you need a reminder on the python syntax follow [this link](https://www.w3schools.com/python/python_arrays.asp)

For example:
Say I am using the testData.csv file

the col headers are

```cs
Timestamp,Price,TradeVolume,TransactionsVolume,HashRate
```

So to add a value Price I can do

```py
Price.append("42069")
```

Remove an element with

```py
Price.pop(index)
```

or

```py
Price.remove("42069")
```

## Printing and checking

### printHeaders

This function prints the current headers or names of the arrays of each row in array format

If the first line of your CSV file is

```CSV
Timestamp,Price,Trade Volume,Transactions Volume,Hash Rate
```

Then

```py

printHeaders()
```

recommendations
will print out

```py
['Timestamp', 'Price', 'TradeVolume', 'TransactionsVolume', 'HashRate']
```

### PrintSmall

The name of this function is kinda bad, if you have recommendations for a better name please go ahead and change it. This function will print out the first three rows

```py
printSmall()
```

will return

```cs
Timestamp,Price,TradeVolume,TransactionsVolume,HashRate
2019-06-27,12933,521683548,361050,57195337
2019-06-28,11133,423175771,407094,57552683
2019-06-29,12374,251088678,356682,59739283
```

If using the testData.csv, can think of it as data.head() in pandas

### printAll

This is self explanatory just prints it in nice formatting

Just use

```
printAll()
```

## Other functions

Other functions that are more specific to the dev but might be useful

### Longest Row

the function `calLongestRow()` as the name suggests returns the length of the longest arrays within your columns

can print it with

```
print(calLongestRow())
```

### Tokenization

Tokenization of a CSV string like

```
foo,bar,fizz,buzz
```

Into

```py
['foo', 'bar', 'fizz', 'buzz']
```

with

```py
tokenizeLine('foo,bar,fizz,buzz')
```
