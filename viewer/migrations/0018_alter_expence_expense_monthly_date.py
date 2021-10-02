# Generated by Django 3.2.7 on 2021-10-02 11:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0017_remove_profile_current_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expence',
            name='expense_monthly_date',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
    ]
