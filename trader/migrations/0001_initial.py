# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-04 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('fee', models.DecimalField(decimal_places=5, default=0.25, max_digits=7)),
            ],
            options={
                'verbose_name': 'Exchange',
            },
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market', models.CharField(choices=[('BTC_BCH', 'BTC_BCH'), ('BTC_ETH', 'BTC_ETH'), ('BTC_DASH', 'BTC_DASH')], help_text='Market', max_length=20)),
                ('type', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], help_text='Trade Type', max_length=20)),
                ('price', models.DecimalField(decimal_places=10, max_digits=19)),
                ('amount_buy', models.DecimalField(decimal_places=10, max_digits=19)),
                ('amount_sell', models.DecimalField(decimal_places=10, max_digits=19)),
                ('amount_usd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fee', models.DecimalField(decimal_places=10, max_digits=19)),
                ('is_success', models.BooleanField(default=False)),
                ('trader', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.Exchange')),
            ],
            options={
                'verbose_name': 'Trade',
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Wallet',
            },
        ),
        migrations.AddField(
            model_name='trade',
            name='wallet_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trades_from', to='trader.Wallet'),
        ),
        migrations.AddField(
            model_name='trade',
            name='wallet_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trades_to', to='trader.Wallet'),
        ),
    ]
