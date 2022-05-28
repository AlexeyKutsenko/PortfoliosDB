from django.contrib import admin
from django.db.models import Sum, Case, When, F

from backtesting_data.models import LazyPortfolio, Ticker, LazyPortfolioTicker


class LazyPortfolioTickerInline(admin.TabularInline):
    model = LazyPortfolioTicker
    autocomplete_fields = (
        'ticker',
    )


class LazyPortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'bond_percentage')
    search_fields = ('name',)
    inlines = [
        LazyPortfolioTickerInline,
    ]

    def get_queryset(self, request):
        base_queryset = super().get_queryset(request)
        return base_queryset.annotate(
            bond_percentage=Sum(
                Case(
                    When(
                        lazyportfolioticker__ticker__type=Ticker.TickerTypes.BONDS,
                        then=F('lazyportfolioticker__weight')
                    ),
                    default=0.0
                )
            )
        ).order_by(
            'bond_percentage'
        )

    def bond_percentage(self, obj):
        return obj.bond_percentage


class TickerAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'type',)
    search_fields = ('symbol',)
    autocomplete_fields = ('equivalents',)


class LazyPortfolioTickerAdmin(admin.ModelAdmin):
    autocomplete_fields = ('portfolio', 'ticker')


admin.site.register(LazyPortfolioTicker, LazyPortfolioTickerAdmin)
admin.site.register(Ticker, TickerAdmin)
admin.site.register(LazyPortfolio, LazyPortfolioAdmin)
