# Generated by Django 3.0.5 on 2020-04-25 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_auto_20200418_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default=datetime.date(2020, 4, 25)),
        ),
    ]
