from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class UserManager(models.Manager):
    def registration_verify(self, postData):
        response = {
            'status' : False,
            'errors' : []
        }
        now = str(datetime.now())
        if len(postData['name'])         < 2:
            response['errors'].append("first name should be at least 3 characters")
        if len(postData['alias'])        < 1:
            response['errors'].append("alias is too short")
        if len(postData['email'])        < 1:
            response['errors'].append("email is too short")
        if len(postData['password'])     < 8:
            response['errors'].append("password too short")
        if postData['confirm_password'] != postData['password']:
            response['errors'].append("passwords do not match")

        # email is or is not valid
        if not re.match(r'[^@]+@[^@]+\.[^@]+', postData['email']):
            response['errors'].append('invalid email change')
        if len(postData['email'])   < 5:
            response['errors'].append("alias should be at least 5 characters")

        # alias  or email not being used
        if len(User.objects.filter(email=postData['email'])):
            response['errors'].append( "this email has already been registered")
            return response
        if len(User.objects.filter(alias=postData['alias'])):
            response['errors'].append( "this alias has already been registered")
            return response

        if len(response['errors']) == 0:
            response['status']  = True
            response['user_id'] = User.objects.create(
            name                = postData['name'],
            alias               = postData['alias'],
            email               = postData['email'],
            password            = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())).id
        return response

        # email and password validation below
    def login_verify(self, postData):

        response = {
            'status' : False,
            'errors' : []
        }
        # BELOW --- ONLY ONE OF THE ERRORS SHOW AT A TIME
        existing_users = (User.objects.filter(email = postData['email']))
        if len(existing_users) == 0:
            response['errors'].append('invalid email')
        else:
            if bcrypt.checkpw(postData['password'].encode(), existing_users[0].password.encode()):
                response['status']  = True
                response['user_id'] = existing_users[0].id
            else:
                response['errors'].append('invalid password')
        return response



class User(models.Model):
    name       = models.CharField(max_length=255)
    email      = models.CharField(max_length=255)
    alias      = models.CharField(max_length=255)
    password   = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects    = UserManager()
