# Generated by Django 3.1.7 on 2021-03-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfileinside', '0006_auto_20210317_1939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Mobile', 'verbose_name_plural': 'Mobiles'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='Turnover_Days',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='Turnover_Days',
            field=models.IntegerField(null=True),
        ),
    ]
