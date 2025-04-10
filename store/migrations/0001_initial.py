# Generated by Django 5.2 on 2025-04-03 13:27

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
                ('product_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
