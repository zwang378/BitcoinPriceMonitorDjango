import urllib.request
import urllib.parse
import json
import heapq

# Create your models here.


class History:
    url = 'https://www.bitstamp.net/api/v2/transactions/btcusd/'
    req = urllib.request.Request(url)

    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))

    price_list = []

    for item in cont:
        price_list.append(item['price'])

    highest_price = heapq.nlargest(1, price_list)
    lowest_price = heapq.nsmallest(1, price_list)


class Bids:
    url = 'https://www.bitstamp.net/api/v2/order_book/btcusd/'
    req = urllib.request.Request(url)

    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))

    bids_list = cont['bids']
    price_list = []
    amount_list = []
    value_list = []

    for index in range(8):
        sublist = bids_list[index]
        value_list.append(float(sublist[0]) * float(sublist[1]))


class Asks:
    url = 'https://www.bitstamp.net/api/v2/order_book/btcusd/'
    req = urllib.request.Request(url)

    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))

    asks_list = cont['asks']
    price_list = []
    amount_list = []
    value_list = []

    for index in range(8):
        sublist = asks_list[index]
        value_list.append(float(sublist[0]) * float(sublist[1]))
