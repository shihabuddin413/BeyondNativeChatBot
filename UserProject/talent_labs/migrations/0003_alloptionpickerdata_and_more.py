# Generated by Django 4.0.5 on 2022-06-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_labs', '0002_alter_jobapplication_job_industry_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllOptionPickerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_industry_option', models.CharField(max_length=500)),
                ('job_type_option', models.CharField(max_length=500)),
                ('working_day_options', models.CharField(max_length=500)),
                ('working_hour_options', models.CharField(max_length=500)),
                ('job_skills_options', models.CharField(max_length=500)),
                ('experince_options', models.CharField(max_length=500)),
                ('pay_types_options', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='required_job_experince',
            field=models.IntegerField(choices=[(1, '1 years'), (2, '1 years'), (3, '1 years'), (4, '1 years'), (5, '5+ years '), (10, '10+ years ')], default='Choose an option'),
        ),
    ]