# Use

If you have used R before this will feel pretty familiar but the whole thing at least to be feels like the rational way of doing things

## Import

To import your file use the function

```py
importData(filename)
```

This will bring all the data from your CSV and init them to arrays with that are named after your headers.

Example:
If I have a csv file like this:

```csv
timestamp,name of user,action,
20-04-2020,the arctesian,sleep,
20-04-2069,daniel,deaded,
```

after importing the data you will get 3 arrays of

```py
timestamp = '20-04-2020', '20-04-69'
nameofuser = 'the arctesian', 'daniel'
action = 'sleep', 'deaded'
```

## addRow

To add a row to your CSV file pass a string of the name of your row to the addRow function

```py
addRow(newRow)
```

this will add the row to the your headers and init a new array with your row name

```py
newRow = []
```

**Warning**

if you pass a rowName like `' Tokenized Values '` this string will be parsed into `'TokenizedValues'`. and to mutate the state of it you will need to use the new parsed value.

## removeRow

This function checks if the rowName is in the headers and removes it

to call it pass the rowName in string format into the function

```py
removeRow('rowName')
```

The same as before please use printHeaders() to check the appropriate row name

## printHeaders

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

## PrintSmall

The name of this function is kinda bad, if you have recommendations for a better name please go ahead and change it. This function will print out the first two roms
