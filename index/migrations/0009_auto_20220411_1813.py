# Generated by Django 3.2.5 on 2022-04-11 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20220411_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='facebook_link',
            field=models.URLField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='instagram_link',
            field=models.URLField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='linkedin_link',
            field=models.URLField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='twitter_link',
            field=models.URLField(max_length=150, null=True),
        ),
    ]
