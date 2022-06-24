from django.shortcuts import render
from .models import Advertisments
from django.http import JsonResponse
# Create your views here.


def sendContentApi(request):
    all_data = list(Advertisments.objects.values())
    return JsonResponse(all_data, safe=False)
