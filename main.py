import requests
from bs4 import BeautifulSoup

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

if __name__ == '__main__':
    temp_coins = fetchCoins()
    coins = filterCoins(temp_coins)

    print(coins)
