# Generated by Django 4.0.5 on 2022-06-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_labs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='job_industry',
            field=models.CharField(choices=[('IT', 'IT'), ('Automobile', 'Automobile'), ('Corporate', 'Corporate'), ('Bank', 'Bank')], default='Choose an option', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_pay_rate_type',
            field=models.CharField(choices=[('Freelancing', 'Freelancing'), ('Contactual', 'Contactual'), ('Monthly', 'Monthly'), ('Weekly', 'Weekly'), ('Yearly', 'Yearly')], default='Choose an option', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_type',
            field=models.CharField(choices=[('Freelancing', 'Freelancing'), ('Contactual', 'Contactual'), ('empolyee', 'As an regular empolyee'), ('Other', 'Others')], default='Choose an option', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='require_job_skill',
            field=models.CharField(choices=[('get_ui_designer', 'Ui designer'), ('developer', ' Developer'), ('site_engineer', 'site engineer')], default='Choose an option', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='required_job_experince',
            field=models.IntegerField(choices=[(1, '1 years'), (2, '1 years'), (3, '1 years'), (4, '1 years'), (5, '5+ years '), (10, '5+ years ')], default='Choose an option'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='working_days',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default='Choose an option'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='working_hours',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default='Choose an option'),
        ),
    ]
