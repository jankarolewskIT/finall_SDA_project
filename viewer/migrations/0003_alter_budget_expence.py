# Generated by Django 3.2.7 on 2021-09-26 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_auto_20210926_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='expence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.expence'),
        ),
    ]