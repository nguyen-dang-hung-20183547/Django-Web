# Generated by Django 3.1.2 on 2020-11-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0014_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='time',
        ),
        migrations.AlterField(
            model_name='cart',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
