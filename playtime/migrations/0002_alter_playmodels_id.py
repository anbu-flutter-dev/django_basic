# Generated by Django 4.1.6 on 2023-03-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playtime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playmodels',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
