# Generated by Django 3.0.5 on 2020-04-19 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='USD', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='income',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
