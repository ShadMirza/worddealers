# Generated by Django 3.2.5 on 2022-04-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20220411_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=50),
        ),
    ]
