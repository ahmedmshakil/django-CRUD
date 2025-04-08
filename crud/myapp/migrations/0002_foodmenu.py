# Generated by Django 5.2 on 2025-04-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.URLField(max_length=60000000000)),
            ],
        ),
    ]
