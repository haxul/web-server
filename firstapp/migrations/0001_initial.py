# Generated by Django 3.0.1 on 2019-12-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Pizza-name')),
                ('description', models.TextField(max_length=400, verbose_name='Description')),
                ('rating', models.FloatField(default=0, verbose_name='Rating')),
                ('url', models.URLField(max_length=500, verbose_name='Shop Link')),
            ],
        ),
    ]
