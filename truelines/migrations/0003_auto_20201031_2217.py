# Generated by Django 3.1.2 on 2020-11-01 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truelines', '0002_auto_20201030_2304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registertable',
            old_name='mobile',
            new_name='mobileno',
        ),
    ]