# Generated by Django 4.0.1 on 2022-01-17 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0003_anketa_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anketa',
            name='yosh',
            field=models.IntegerField(max_length=30),
        ),
    ]
