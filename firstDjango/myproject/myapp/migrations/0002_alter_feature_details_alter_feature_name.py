# Generated by Django 4.1.2 on 2022-11-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='details',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
