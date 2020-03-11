# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DailyLine(models.Model):
    id = models.AutoField(primary_key=True, max_length=32)
    ts_code = models.CharField(max_length=32, blank=True, null=True)
    trade_date = models.CharField(max_length=32, blank=True, null=True)
    open = models.CharField(max_length=32, blank=True, null=True)
    high = models.CharField(max_length=32, blank=True, null=True)
    low = models.CharField(max_length=32, blank=True, null=True)
    close = models.CharField(max_length=32, blank=True, null=True)
    pre_close = models.CharField(max_length=32, blank=True, null=True)
    change = models.CharField(max_length=32, blank=True, null=True)
    pct_chg = models.CharField(max_length=32, blank=True, null=True)
    vol = models.CharField(max_length=32, blank=True, null=True)
    amount = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'daily_line'


class StockBasic(models.Model):
    index = models.AutoField(primary_key=True)
    ts_code = models.CharField(max_length=45, blank=True, null=True)
    symbol = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    area = models.CharField(max_length=45, blank=True, null=True)
    industry = models.CharField(max_length=45, blank=True, null=True)
    fullname = models.CharField(max_length=45, blank=True, null=True)
    enname = models.CharField(max_length=128, blank=True, null=True)
    market = models.CharField(max_length=45, blank=True, null=True)
    exchange = models.CharField(max_length=45, blank=True, null=True)
    curr_type = models.CharField(max_length=45, blank=True, null=True)
    list_status = models.CharField(max_length=45, blank=True, null=True)
    list_date = models.CharField(max_length=45, blank=True, null=True)
    delist_date = models.CharField(max_length=45, blank=True, null=True)
    is_hs = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_basic'


class Test(models.Model):
    index = models.IntegerField(primary_key=True)
    string = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
