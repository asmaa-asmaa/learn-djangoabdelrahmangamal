# Generated by Django 5.1.3 on 2024-11-25 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_product_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
