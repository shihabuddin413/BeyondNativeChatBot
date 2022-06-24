# Generated by Django 4.0.5 on 2022-06-21 03:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Type Advertisment Title Here', max_length=200)),
                ('content', models.TextField(help_text='Type Or Paste Your Content Here')),
                ('publish_date', models.DateField(default=django.utils.timezone.now, help_text='The day you want to scheduled this advertisment')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
