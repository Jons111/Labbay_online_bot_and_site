# Generated by Django 4.0.1 on 2022-01-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('fam', models.CharField(max_length=30)),
                ('yosh', models.EmailField(max_length=30)),
                ('tel', models.CharField(max_length=20)),
                ('jins', models.CharField(max_length=20)),
                ('shaxar', models.CharField(max_length=20)),
            ],
        ),
    ]