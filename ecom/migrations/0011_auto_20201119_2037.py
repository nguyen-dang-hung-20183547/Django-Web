# Generated by Django 3.1.2 on 2020-11-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0010_auto_20201119_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cpu',
            field=models.TextField(default=''),
        ),
    ]
