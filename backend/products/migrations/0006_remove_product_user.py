# Generated by Django 4.0.10 on 2025-01-20 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
