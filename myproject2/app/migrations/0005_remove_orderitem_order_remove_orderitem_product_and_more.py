# Generated by Django 5.1.1 on 2024-10-24 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_added_on_cart_created_at_remove_cart_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
    ]
