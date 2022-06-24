
from django.db import models


# Create your models here.
class AllOptionPickerData(models.Model):

    help_text_inp = "Options must be separated by comma with each other"
    job_industry_option = models.TextField(help_text=help_text_inp)
    job_type_option = models.TextField(help_text=help_text_inp)
    working_day_options = models.TextField(help_text=help_text_inp)
    working_hour_options = models.TextField(help_text=help_text_inp)
    job_skills_options = models.TextField(help_text=help_text_inp)
    experince_options = models.TextField(help_text=help_text_inp)
    pay_types_options = models.TextField(help_text=help_text_inp)

    def __str__(self):
        return "default"


class JobApplication (models.Model):
    pay_types = job_type = working_days_choice = working_hr_choice = job_skills = job_industry = experince = ()
    item = AllOptionPickerData.objects.all()[0]
    pay_types = ((i, i) for i in item.pay_types_options.split(','))
    job_type = ((i, i) for i in item.job_type_option.split(','))
    working_days_choice = ((int(i), i)
                           for i in item.working_day_options.split(','))
    working_hr_choice = ((int(i), i)
                         for i in item.working_hour_options.split(','))
    pay_types = ((i, i) for i in item.pay_types_options.split(','))
    job_skills = ((i, i) for i in item.job_skills_options.split(','))
    job_industry = ((i, i) for i in item.job_industry_option.split(','))
    experince = ((int(i), i+" years")
                 for i in item.experince_options.split(','))

    job_title = models.CharField(max_length=100, default="job title")
    job_description = models.TextField()
    job_vacancy = models.IntegerField()
    job_location = models.CharField(max_length=100)
    working_days = models.IntegerField(
        choices=working_days_choice, default="Choose an option")
    working_hours = models.IntegerField(
        choices=working_hr_choice, default="Choose an option")
    job_type = models.CharField(
        max_length=50, choices=job_type, default="Choose an option")
    job_industry = models.CharField(
        max_length=50, choices=job_industry, default="Choose an option")
    salary_expectation = models.IntegerField()
    job_pay_rate_type = models.CharField(
        max_length=100, choices=pay_types, default="Choose an option")
    required_job_experince = models.IntegerField(
        choices=experince, default="Choose an option")
    require_job_skill = models.CharField(
        max_length=100, choices=job_skills, default="Choose an option")

    def __str__(self):
        return self.job_title
