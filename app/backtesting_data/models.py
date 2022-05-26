from django.db import models


class LazyPortfolio(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ticker(models.Model):
    symbol = models.CharField(max_length=100)
    portfolio = models.ManyToManyField(LazyPortfolio, through="LazyPortfolioTicker")
    equivalents = models.ManyToManyField("self", null=True, blank=True)
    inception_date = models.DateField()

    def __str__(self):
        return self.symbol


class LazyPortfolioTicker(models.Model):
    portfolio = models.ForeignKey(LazyPortfolio, models.CASCADE)
    ticker = models.ForeignKey(Ticker, models.CASCADE)
    percentage = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.portfolio} {self.ticker} {self.percentage}'
