from django.contrib import admin

from backtesting_data.models import LazyPortfolio, Ticker, LazyPortfolioTicker


class LazyPortfolioTickerInline(admin.TabularInline):
    model = LazyPortfolioTicker


class LazyPortfolioAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    inlines = [
        LazyPortfolioTickerInline,
    ]


class TickerAdmin(admin.ModelAdmin):
    search_fields = ('symbol',)
    autocomplete_fields = ('equivalents',)


class LazyPortfolioTickerAdmin(admin.ModelAdmin):
    autocomplete_fields = ('portfolio', 'ticker')


admin.site.register(LazyPortfolioTicker, LazyPortfolioTickerAdmin)
admin.site.register(Ticker, TickerAdmin)
admin.site.register(LazyPortfolio, LazyPortfolioAdmin)
