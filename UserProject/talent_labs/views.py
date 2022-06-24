from django.shortcuts import render
from .forms import JobApplicationForm
from .models import AllOptionPickerData, JobApplication
from django.http import JsonResponse


def JobApplicationDataApi(request):
    if len(request.GET) == 0:
        all_data = list(JobApplication.objects.values())
        return JsonResponse(all_data, safe=False)

    job_industry = request.GET['job_industry']
    job_skill = request.GET['job_skill']
    select_data = list(JobApplication.objects.values().filter(job_industry__icontains=job_industry, require_job_skill__icontains=job_skill))

    return JsonResponse(select_data, safe=False)


def AllOptionPickerDataApi(request):
    all_data = list(AllOptionPickerData.objects.values())
    return JsonResponse(all_data, safe=False)

# Create your views here.


def JobApplicationHandler(request):
    form = JobApplicationForm()
    context = {'form': form}
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            "success": "Job Has been added successfully. Checkout using above buttton..."}
        return render(request, 'job_form.html', context)
    return render(request, 'job_form.html', context)
