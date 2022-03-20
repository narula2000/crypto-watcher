# Crypto Watcher

This project was created for me to better understand Pandas library and uses
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
- bash

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
--------------------------Today: 2021-12-03---------------------------
++++++++++++++++++++++Top 15 Coins by Marketcap+++++++++++++++++++++++
===============================Bitcoin================================
       Current       Mean  Moving Mean  PC Mean  PC Moving Mean
1m   56921.902  60162.690    60247.249   -5.387          -5.519
3m   56921.902  55049.605    55718.403    3.401           2.160
6m   56921.902  47003.298    47021.157   21.102          21.056
12m  56921.902  45354.117    45749.350   25.505          24.421
===============================Ethereum===============================
      Current      Mean  Moving Mean  PC Mean  PC Moving Mean
1m   4575.444  4444.780     4401.376    2.940           3.955
3m   4575.444  3886.578     3863.161   17.724          18.438
6m   4564.237  3217.540     3189.115   41.855          43.119
12m  4575.444  2514.926     2516.980   81.932          81.783
=============================Binance Coin=============================
     Current     Mean  Moving Mean  PC Mean  PC Moving Mean
1m   618.539  607.588      604.656    1.802           2.296
3m   618.539  495.604      488.262   24.805          26.682
6m   618.539  425.409      418.140   45.399          47.926
12m  618.539  338.129      339.294   82.930          82.302
================================Solana================================
     Current     Mean  Moving Mean  PC Mean  PC Moving Mean
1m   232.773  225.456      222.823    3.245           4.465
3m   232.773  185.360      184.411   25.579          26.225
6m   232.773  114.817      113.408  102.733         105.252
12m  232.773   66.245       63.942  251.382         264.036
...
```
