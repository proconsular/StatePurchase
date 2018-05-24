from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.db.models import Q

def prompt(request):

    request.session.flush()
    return render(request,'login_registration/login.html')

def register(request):

    return render(request,'login_registration/register.html')

def create(request):
    result = User.objects.registration_verify(request.POST)
    if result['status']:
        request.session['user_id'] = result['user_id']
        return redirect('/home')
    else:
        for error in result['errors']:
            messages.error(request, error)
        return redirect('/register')

def login(request):
    result = User.objects.login_verify(request.POST)
    if result['status']:
        request.session['user_id'] = result['user_id']
        return redirect('/home')
    else:
        for error in result['errors']:
            messages.error(request, error)
    return redirect('/state_purchase')



# BELOW IS AFTER LOGIN OR REGISTRATION
def home(request):
    # if 'user_id' in request.session:
    #     context = {
    #     'curr_user' : User.objects.get(id = request.session['user_id']),
    # }
    #     return render(request,'login_registration/success.html', context)
    # else:
        # RIGHT NOW THIS ONLY TAKES YOU BACK TO THE LOGIN PAGE, NOT REGISTER
    return redirect('/state_purchase')

def logout(request):
    request.session.flush()
    return redirect('/state_purchase')