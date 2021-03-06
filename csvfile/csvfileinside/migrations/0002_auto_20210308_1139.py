# Generated by Django 3.1.1 on 2021-03-08 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfileinside', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='All_Stock',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Average_Flow',
            field=models.DecimalField(decimal_places=3, max_digits=10, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Sales_Proportion',
            field=models.DecimalField(decimal_places=3, max_digits=10, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Sales_Volume',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Statistics_Model',
            field=models.TextField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Stock_Proportion',
            field=models.DecimalField(decimal_places=3, max_digits=10, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Turnover_Days',
            field=models.TextField(max_length=10, null=True),
        ),
    ]
