# Generated by Django 4.0.10 on 2025-01-20 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
    ]
