# Generated by Django 3.1.7 on 2021-03-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfileinside', '0005_auto_20210317_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='Turnover_Days',
            field=models.IntegerField(max_length=10,null=True),
        ),
    ]
