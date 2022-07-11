# coalas

[![PyPI Latest Release](https://img.shields.io/pypi/v/coalas.svg)](https://pypi.org/project/coalas/)
[![License](https://img.shields.io/pypi/l/coalas.svg)](https://github.com/theArctesian/coalas/blob/main/LICENSE)

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

Thank you for wanting to contribute, please look at the todo file for task that remain unfinished, or audit the code. In general use your rational judgment, don't submit anything malicious or project breaking, I or any maintainers will check. Don't be afraid to do anything radical or delete large swaths of code, take risks and innovate.

The only requirement I will set is that you write a log of your work in the `log.md` file. Follow the format. This **must be done** before and after every session. While this might seem tedious and monotonous, it allows me other to acknowledge the effort you have put it to helping the open source community. It as also fun to go back read anecdotes and relive the pain or jubilation the past.

## Thanks

Thanks to @Stelercus for the name, had to change it to `coalas` instead of `koalas` because `koalas` wass already taken

## Donate address 
Eth
```
0xc7AfE4114E3b78cB22Ec7EbDA11AD40199a9Cb96
```
Cardano:
```
addr1q85kef4y4zx4lyxyuq3wgec3nddn53wv6nmydrc6eyx5l47jdatz0hja95dudtxclcjp8ejkthl6hl5xjfregk9lllrs8um6c0
```

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
