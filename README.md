# coalas

## Overview

This aims to be the simplest way of handling CSV files.

I was pissed off with how pandas handled data, so I think I am going to make my own. Also pandas has a data limit of 50MB which is kinda stupid I may also be using it wrong. But anyways this is limited to the ram in your computer so have fun.

## Install

```sh
pip install coalas
```

## Upgrade

```sh
pip install coalas --upgrade
```

## Use

At the begging of your file import the data using the function

```py
from coalas import coalas as c
c.importData("filename")
c.printAll()
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

You can the mutate the state of the arrays with normal python functionality

For more info please check the docs folder

## Contributing

If anyone would like to contribute take a look at the todo.md for this needed.

Comments are always necessary, ik I might have overdone the comments but it is a better problem to have then no comments.

Please write log file in log.md when you are done and follow the format.

## Thanks

Thanks to @Stelercus for the name, had to change it to `coalas` instead of `koalas` because `koalas` wass already taken

## Info

```

email (business) : me@danielokita.com
twitter : @theArctesian
discord : 0xArctesian#8968
telegram : @TheArctesian
signal : @Arctesian

```

## <span style="color: red"> PSA!! </span>

This project is licensed under [GPL-3](https://www.gnu.org/licenses/quick-guide-gplv3.html). If you have a problem with it cry about it. In short, any fork of this project must maintain the license and adhere to the 4 essential freedoms of free software as listed by the [FSF](https://www.gnu.org/philosophy/free-sw.en.html).
