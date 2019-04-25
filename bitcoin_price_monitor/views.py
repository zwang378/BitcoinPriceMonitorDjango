from django.shortcuts import render

from .models import History, Bids, Asks


def index(request):
    return render(request, 'bitcoin_price_monitor/index.html')


def history(request):

    recent_history = History

    return render(request, 'bitcoin_price_monitor/history.html', {'recent_history': recent_history})


def bids(request):

    recent_bids = Bids

    return render(request, 'bitcoin_price_monitor/bids.html', {'recent_bids': recent_bids})


def asks(request):

    recent_asks = Asks

    return render(request, 'bitcoin_price_monitor/asks.html', {'recent_asks': recent_asks})
