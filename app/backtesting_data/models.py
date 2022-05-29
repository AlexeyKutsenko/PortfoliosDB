import csv

from django.db import models
from django.utils.translation import gettext_lazy as _
from sanitize_filename import sanitize


class LazyPortfolio(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def make_csv(self, path):
        full_path = path / sanitize(f'{self.name}.csv')
        with open(full_path, 'w+') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(['Symbol, Weight'])
            for portfolio_ticker in self.lazyportfolioticker_set.all():
                writer.writerow([portfolio_ticker.ticker.symbol, f'{portfolio_ticker.weight}%'])


class Ticker(models.Model):
    class TickerTypes(models.TextChoices):
        BONDS = 'Bonds', _('Bonds')
        COMMODITIES = 'Comm', _('Commodities')
        STOCKS = 'Stocks', _('Stocks')

    equivalents = models.ManyToManyField("self", blank=True)
    expense_ratio = models.FloatField()
    inception_date = models.DateField()
    portfolio = models.ManyToManyField(LazyPortfolio, through="LazyPortfolioTicker")
    symbol = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=10, choices=TickerTypes.choices, default=TickerTypes.STOCKS)

    def __str__(self):
        return self.symbol


class LazyPortfolioTicker(models.Model):
    portfolio = models.ForeignKey(LazyPortfolio, models.CASCADE)
    ticker = models.ForeignKey(Ticker, models.CASCADE)
    weight = models.FloatField(null=False)

    def __str__(self):
        return f'{self.portfolio} {self.ticker} {self.weight}'
