# Generated by Django 4.0.5 on 2022-06-21 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussines_brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisments',
            name='media',
            field=models.CharField(default='', help_text='Type Or Paste Your Media Link Here', max_length=300),
        ),
    ]
