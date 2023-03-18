# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agent(models.Model):
    agent_code = models.CharField(db_column='AGENT_CODE', primary_key=True, max_length=6)  # Field name made lowercase.
    agent_name = models.CharField(db_column='AGENT_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    working_area = models.CharField(db_column='WORKING_AREA', max_length=35, blank=True, null=True)  # Field name made lowercase.
    commission = models.DecimalField(db_column='COMMISSION', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    phone_no = models.CharField(db_column='PHONE_NO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'agent'


class Customer(models.Model):
    cust_code = models.CharField(db_column='CUST_CODE', primary_key=True, max_length=6)  # Field name made lowercase.
    cust_name = models.CharField(db_column='CUST_NAME', max_length=40)  # Field name made lowercase.
    cust_city = models.CharField(db_column='CUST_CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    working_area = models.CharField(db_column='WORKING_AREA', max_length=35)  # Field name made lowercase.
    cust_country = models.CharField(db_column='CUST_COUNTRY', max_length=20)  # Field name made lowercase.
    grade = models.DecimalField(db_column='GRADE', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    opening_amt = models.DecimalField(db_column='OPENING_AMT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    receive_amt = models.DecimalField(db_column='RECEIVE_AMT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    payment_amt = models.DecimalField(db_column='PAYMENT_AMT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    outstanding_amt = models.DecimalField(db_column='OUTSTANDING_AMT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    phone_no = models.CharField(db_column='PHONE_NO', max_length=17)  # Field name made lowercase.
    agent_code = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AGENT_CODE')  # Field name made lowercase.

    class Meta:
        db_table = 'customer'


class Order(models.Model):
    ord_num = models.DecimalField(db_column='ORD_NUM', primary_key=True, max_digits=6, decimal_places=0)  # Field name made lowercase.
    ord_amount = models.DecimalField(db_column='ORD_AMOUNT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    advance_amount = models.DecimalField(db_column='ADVANCE_AMOUNT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    ord_date = models.DateField(db_column='ORD_DATE')  # Field name made lowercase.
    cust_code = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CUST_CODE')  # Field name made lowercase.
    agent_code = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AGENT_CODE')  # Field name made lowercase.
    ord_description = models.CharField(db_column='ORD_DESCRIPTION', max_length=60)  # Field name made lowercase.

    class Meta:
        db_table = 'order'
