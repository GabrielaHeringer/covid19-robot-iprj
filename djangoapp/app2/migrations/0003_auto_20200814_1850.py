# Generated by Django 3.0.5 on 2020-08-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_auto_20200814_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='data_nascimento',
            field=models.DateField(),
        ),
    ]
