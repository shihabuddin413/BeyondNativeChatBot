from django.shortcuts import render, redirect
import mysql.connector as sql

first_name = last_name = sex = email = password = ''

# Create your views here.
def ShowSignUpPage(request):
    global first_name, last_name, sex, email, password
    if request.method == "POST":
        m = sql.connect(host='localhost',
                        user='root',
                        passwd="RTSshihab413",
                        database="telegram_bot")
        cursor = m.cursor()
        d = request.POST
        for key, val in d.items():
            if(key == 'first_name'):
                first_name = val
            if(key == 'last_name'):
                last_name = val
            if(key == 'sex'):
                sex = val
            if(key == 'email'):
                email = val
            if(key == 'password'):
                password = val
        cmd = "INSERT INTO users VALUES('{}','{}','{}','{}', '{}')".format(
            first_name, last_name, sex, email, password)
        try:
            cursor.execute(cmd)
            m.commit()
        except:
            return render(request,'signup.html',{"error":"There is an error occured please check if email is unique"})

    return render(request, 'signup.html')
