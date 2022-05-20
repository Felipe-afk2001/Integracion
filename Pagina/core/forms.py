from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from adminapp.models import usuarios

class user_form (ModelForm):
    class Meta :
        model=usuarios
        fields='__all__'
