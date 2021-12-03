import datetime as dt

import pandas as pd
import pandas_datareader as web
import requests
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta

def fetchCoins():
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
    unwanted = set(['USDT', 'USDC', 'WBTC', 'UNI', 'BUSD'])
    lst = []
    for coin in coins:
        if coin[0] not in unwanted:
            lst.append(coin)
    return lst

def fetchPrice(symbol='BTC-USD', gap=6, day=False):
    end = dt.datetime.now()
    start = end - relativedelta(months=gap)
    if day:
        start = end - relativedelta(days=gap)
    return web.DataReader(symbol, 'yahoo', start, end)

def getChange(current, previous):
    if current == previous:
        return 0
    try:
        return ((current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return float('inf')

if __name__ == '__main__':
    temp_coins = fetchCoins()
    coins = filterCoins(temp_coins)

    print(coins)

    time_gaps = [1, 3, 6, 12]
    months = ['1m', '3m', '6m', '12m']
    for coin in coins:
        symbol, name = coin
        symbol_usd = f'{symbol}-USD'
        currents, means, changes = [], [], []
        for gap in time_gaps:
            try:
                pd.DataFrame(fetchPrice(symbol=symbol_usd, gap=gap))
            except:
                symbol_usd = f'{symbol}1-USD'

            data = pd.DataFrame(fetchPrice(symbol=symbol_usd, gap=gap))
            close = data['Close']

            current = close[-1]
            mean = close.mean()
            change = getChange(current, mean)

            if round(current, 3) < 0.001:
                currents.append(current)
                means.append(mean)
                changes.append(change)
            else:
                currents.append(round(current, 3))
                means.append(round(mean, 3))
                changes.append(round(change, 3))

        df = pd.DataFrame(data={
            'Current': currents,
            'Mean': means,
            '% Change': changes
        }, index=months)
        print(df)
