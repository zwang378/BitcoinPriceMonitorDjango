from django.urls import path

from . import views


app_name = 'bitcoin_price_monitor'
urlpatterns = [
    path('', views.index, name='index'),
    path('history', views.history, name='history'),
    path('bids', views.bids, name='bids'),
    path('asks', views.asks, name='asks'),
]


