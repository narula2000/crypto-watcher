# Crypto Watcher

This project was created to for me to better understand Pandas library and uses
BeautifulSoup for web scrapping. The purpose of the project is to compare the
average cryptocurrency price from the different month gap to the current price.

## Language Requirement

- Python >= 3.6

This is due to the need of Pipenv.

## Library Used

Python

- pandas
- pandas-datareader
- beautifulsoup4
- python-dateutil

Operating System

- xclip

## Quick Start

For outputting the table:

```bash
pipenv run python3 main.py
```

For saving as a file and copy to clipboard:

```bash
./update.sh
```

## Example Output

```
----------Today: 2021-12-03-----------
++++++Top 15 Coins by Marketcap+++++++
===============Bitcoin================
       Current       Mean  % Change
1m   56319.633  60143.262    -6.358
3m   56354.949  55043.443     2.383
6m   56354.949  47000.217    19.904
12m  56354.949  45352.568    24.260
===============Ethereum===============
      Current      Mean  % Change
1m   4499.629  4442.334     1.290
3m   4499.629  3885.754    15.798
6m   4499.629  3217.189    39.862
12m  4499.629  2514.719    78.932
=============Binance Coin=============
     Current     Mean  % Change
1m   613.449  607.424     0.992
3m   613.449  495.549    23.792
6m   613.449  425.381    44.211
12m  613.449  338.115    81.432
================Solana================
     Current     Mean  % Change
1m   228.295  225.312     1.324
3m   228.295  185.311    23.196
6m   228.295  114.793    98.876
12m  228.295   66.233   244.687
...
```
