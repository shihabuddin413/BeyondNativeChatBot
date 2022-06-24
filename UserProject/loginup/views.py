from django.shortcuts import render, redirect
import mysql.connector as sql

email = password = ""
# Create your views here.
def ShowLoginPage(request):
    global email, password
    t=None
    if request.method == "POST":
        m = sql.connect(host='localhost',
                        user='root',
                        passwd="RTSshihab413",
                        database="telegram_bot")
        cursor = m.cursor()
        d = request.POST
        for key, val in d.items():
            if(key == 'email'):
                email = val
            if(key == 'password'):
                password = val
        cmd = "SELECT * FROM users WHERE email='{}' and password='{}'".format(email, password)
        cursor.execute(cmd)
        t = tuple(cursor.fetchall())
        if t==():
            return render (request, 'login.html',  {'error':'Please enter correct email and password' })
        else :
            return render (request, 'bording.html',
                            { 'msg': 'Welcome to on bording job service. Now please use our bot for an interactive experince!', 
                            'link':"https://t.me/Rts38900bot", 
                            'username':t[0][0]+' '+t[0][1] } )

    return render(request, 'login.html') 