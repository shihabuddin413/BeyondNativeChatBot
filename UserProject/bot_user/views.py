
from django.shortcuts import render
from .forms import SignUpForm, LoginForm
from .models import BotUsers


def ShowLoginPage(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            usr_email = request.POST['email']
            usr_password = request.POST['password']
            all_bot_users = BotUsers.objects.all()
            for usr in all_bot_users:
                if (usr.email == usr_email and usr.password == usr_password):
                    username = usr.first_name + ' ' + usr.last_name
                    return render(request, 'bording.html',
                                  {'msg': 'Welcome to on bording job service. Now please use our bot for an interactive experince!',
                                   'link': "https://t.me/Rts38900bot",
                                   'username': username})

        return render(request, 'login.html', {"error": "please enter email & password correctly"})

    return render(request, 'login.html')


def ShowSignUpPage(request):
    if request.method == "POST":
        try:
            all_bot_users = BotUsers.objects.all()
            email = request.POST['email']
            username = request.POST['first_name'] + \
                ' ' + request.POST['last_name']
            form = SignUpForm(request.POST)
            unique_email = True
            for data in all_bot_users:
                if data.email == email:
                    unique_email = False
                    return render(request, 'signup.html', {'error': 'Email should be unique'})

            if form.is_valid() and unique_email:
                form.save()
                return render(request, 'bording.html',
                              {'msg': 'Welcome to on bording job service. Now please use our bot for an interactive experince!',
                               'link': "https://t.me/Rts38900bot",
                               'username': username})
            else:
                return render(request, 'signup.html', {'error': 'Please fill up all the fields'})

        except:
            return render(request, 'signup.html', {"error": "Sorry! There is an error occured please check if email is unique"})

    return render(request, 'signup.html')
