# Generated by Django 5.1.3 on 2024-11-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
