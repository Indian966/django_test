# Generated by Django 3.2.13 on 2022-06-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220629_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cop',
            name='cop_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cop',
            name='region',
            field=models.CharField(blank=True, default='korea', max_length=100),
        ),
    ]
