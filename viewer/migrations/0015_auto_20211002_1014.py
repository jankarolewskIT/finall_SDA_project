# Generated by Django 3.2.7 on 2021-10-02 10:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0014_alter_expence_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='expence',
            name='expense_monthly_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='expence',
            name='is_cycle',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='income_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pay_day',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
    ]
