from django.contrib import admin

# Register your models here.
from .models import JobApplication, AllOptionPickerData


admin.site.register(AllOptionPickerData)
admin.site.register(JobApplication)
