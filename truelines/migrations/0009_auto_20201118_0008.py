# Generated by Django 3.1.2 on 2020-11-18 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truelines', '0008_auto_20201118_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotespost',
            name='quotes',
            field=models.CharField(max_length=500),
        ),
    ]