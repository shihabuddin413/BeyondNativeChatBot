"""UserProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bot_user.views import ShowSignUpPage, ShowLoginPage
# from signup.views import ShowSignUpPage
# from loginup.views import ShowLoginPage
from bussines_brand.views import sendContentApi
from talent_labs.views import JobApplicationHandler, JobApplicationDataApi, AllOptionPickerDataApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ShowSignUpPage),
    path('login/', ShowLoginPage),
    path('store-job-application-form/', JobApplicationHandler),
    path('api/get/job-application-data/', JobApplicationDataApi),
    path('api/get/all-options-data/', AllOptionPickerDataApi),
    path('api/get/content/',sendContentApi)
]
