#/usr/bin/python 
#coding: utf8

from django import forms
from models import *


class PiSettingsForm(forms.ModelForm):  
    class Meta:  
        model = PiSettings  

class PiAccountForm(forms.ModelForm):
    class Meta:
            model = PiUser
            fields = ('first_name','last_name')

    password1 = forms.CharField(required=False, widget=forms.PasswordInput,label='Password', initial="")
    password2 = forms.CharField(required=False, widget=forms.PasswordInput,label='Confirm password', initial="")

    def clean(self):
        cleaned_data = super(PiAccountForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2:
            if password1!=password2:
                msg = u"Password not Same"
                self._errors["password2"] = self.error_class([msg])
        return cleaned_data

class PiRegisterForm(forms.ModelForm):
    class Meta:
            model = PiUser
            fields = ('first_name','last_name','email')

    password1 = forms.CharField(widget=forms.PasswordInput,label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput,label='Confirm password')

    def clean(self):
        cleaned_data = super(PiRegisterForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2:
            if password1!=password2:
                msg = u"Password not Same"
                self._errors["password2"] = self.error_class([msg])
        return cleaned_data