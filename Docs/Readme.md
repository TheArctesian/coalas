# Use

To import your file use the function

```py
importData(filename)
```

If you want to write to a file

```py
writeData(filename)
```

# Warning

I do this in kinda a lazy way by updating global vars and shit so DON'T USE THESE VARS

- ColHeaders
- TokenHeaders
- lineCount
- ra
- {THE NAMES OF YOUR COL HEADERS}
  If I had a CSV file that looks like
  ```csv
  index,price
  1,69
  2,420
  ```
  DON'T USE index or price as var names
