# Generated by Django 4.1.13 on 2023-12-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=200, unique_for_date='publish'),
        ),
    ]
