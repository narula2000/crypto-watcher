import datetime as dt

import pandas as pd
import pandas_datareader as web
import requests
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta


def fetchCoins():
    """Web Scrap CoinMarketCap for top coins by marketcap.

    Returns: lst[(str, str)]: List of top coins.

    """

    url = 'https://coinmarketcap.com/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table_body = soup.find('tbody')
    rows = table_body.findAll('tr')
    top10 = rows[:10]
    rest20 = rows[11:21]

    coins = []
    for row in top10:
        data_cell = row.findAll('td')
        coin = data_cell[2].findAll('p')
        name, symbol = coin[0].getText(), coin[1].getText()
        coins.append((symbol, name))

    for row in rest20:
        data_cell = row.findAll('td')
        coin = data_cell[2].findAll('span')
        name, symbol = coin[1].getText(), coin[2].getText()
        coins.append((symbol, name))

    return coins


def filterCoins(coins):
    """Filtering Coins to useful ones.

    Parameters:
    coins (lst[(str, str)]): Cryptocurreny Index

    Returns:
    lst[(str, str)]: List of coins we want to fetch for.

    """
    unwanted = set(['USDT', 'USDC', 'BUSD', 'UST', 'WBTC','DAI', 'CRO'])

    filtered = filter(lambda coin: coin[0] not in unwanted, coins)
    return list(filtered)


def fetchPrice(symbol='BTC-USD', gap=6, day=False):
    """Fetch Price from Yahoo Database.

    Parameters:
    symbol (str): Cryptocurreny Index
    gap (int): Amount of time gap for the data range
    day (boolean): Falg to change gap from months to days

    Returns:
    pd.DataFrame: Yahoo Finanace dataframe of the crypto index.

    """

    end = dt.datetime.now()
    start = end - relativedelta(months=gap)
    if day:
        start = end - relativedelta(days=gap)
    return web.DataReader(symbol, 'yahoo', start, end)


def getChange(current, previous):
    """Get the Percentage Change.

    Parameters:
    current (int): Current value
    previous (int): Previous value

    Returns:
    int: Percentage Change

    """

    if current == previous:
        return 0
    try:
        return ((current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return float('inf')


def printHeader(name, char='=', length=70):
    """Print Header with surround chars

    Parameters:
    name (str): Heading we want to print
    char (str): Character we want to surround the header
    length (int): Length of the Header

    Returns:
    None: Print the header with the given string.

    """

    print(name.center(length, char))


if __name__ == '__main__':
    temp_coins = fetchCoins()
    coins = filterCoins(temp_coins)

    toady_string = 'Today: ' + str(dt.datetime.now().date())
    printHeader(toady_string, '-')
    printHeader(f'Top {len(coins)} Coins by Marketcap', '+')

    time_gaps = [1, 3, 6, 12]
    months = ['1m', '3m', '6m', '12m']
    for coin in coins:
        symbol, name = coin
        symbol_usd = f'{symbol}-USD'
        if symbol == 'DOGE':
            symbol_usd = f'{symbol}COIN-USD'
        currents, means, moving_means, changes, moving_changes = [], [], [], [], []
        printHeader(name)
        for gap in time_gaps:
            try:
                pd.DataFrame(fetchPrice(symbol=symbol_usd, gap=gap))
            except:
                symbol_usd = f'{symbol}1-USD'

            data = pd.DataFrame(fetchPrice(symbol=symbol_usd, gap=gap))
            close = data['Close']

            current = close[-1]
            mean = close.mean()
            moving_mean = close.rolling(window=20).mean().mean()
            change = getChange(current, mean)
            moving_change = getChange(current, moving_mean)

            # Display coins which have USD value lower than 0.001
            if round(current, 3) < 0.001:
                currents.append(current)
                means.append(mean)
                moving_means.append(moving_mean)
                changes.append(change)
                moving_changes.append(moving_change)
            else:
                currents.append(round(current, 3))
                means.append(round(mean, 3))
                moving_means.append(round(moving_mean, 3))
                changes.append(round(change, 3))
                moving_changes.append(round(moving_change, 3))

        df = pd.DataFrame(data={
            'Current': currents,
            'Mean': means,
            'Moving Mean': moving_means,
            'PC Mean': changes,
            'PC Moving Mean': moving_changes
        }, index=months)
        print(df)
