# Generated by Django 4.0.1 on 2022-01-18 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0006_alter_anketa_yosh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sotib_olingan_maxsulotlar',
            name='rasm1',
        ),
        migrations.AlterField(
            model_name='sotib_olingan_maxsulotlar',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
