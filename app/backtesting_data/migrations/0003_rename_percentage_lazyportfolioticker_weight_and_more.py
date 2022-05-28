# Generated by Django 4.0.4 on 2022-05-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtesting_data', '0002_alter_lazyportfolioticker_percentage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lazyportfolioticker',
            old_name='percentage',
            new_name='weight',
        ),
        migrations.AddField(
            model_name='ticker',
            name='expense_ratio',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticker',
            name='type',
            field=models.CharField(choices=[('Bonds', 'Bonds'), ('Comm', 'Commodities'), ('Stocks', 'Stocks')], default='Stocks', max_length=10),
        ),
    ]
