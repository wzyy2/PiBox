#coding=utf-8
'''
# The modules contains PiApp's forms 

# Any issues or improvements please contact jacob-chen@iotwrt.com
'''

#/usr/bin/python 
#coding: utf8

from django import forms
from models import *


class PiSettingsForm(forms.ModelForm):  
    class Meta:  
        model = PiSettings  
        fields = ('ip','port', 'enable_register')
    def __init__(self, *args, **kwargs):
        super(PiSettingsForm, self).__init__(*args, **kwargs)
        self.fields['ip'].widget.attrs.update({'class' : 'form-control'})
        self.fields['port'].widget.attrs.update({'class' : 'form-control'})
        self.fields['enable_register'].widget.attrs.update({'class' : 'form-control'})

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


class DeviceForm(forms.ModelForm):
    class Meta:
            model = Device
            fields = ('name','describe','location','x','y')    

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['describe'].widget.attrs.update({'class' : 'form-control'})
        self.fields['location'].widget.attrs.update({'class' : 'form-control'})
        self.fields['x'].widget.attrs.update({'class' : 'form-control'})
        self.fields['y'].widget.attrs.update({'class' : 'form-control'})

class HomeForm(forms.ModelForm):
    class Meta:
            model = Home
            fields = ('name','img',)                

    def __init__(self, *args, **kwargs):
        super(HomeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})


class SensorForm(forms.ModelForm):
    class Meta:
            model = Sensor
            fields = ('name','describe','sensor_class','unit')             

    def __init__(self, *args, **kwargs):
        super(SensorForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})  
        self.fields['describe'].widget.attrs.update({'class' : 'form-control'})  
        self.fields['sensor_class'].widget.attrs.update({'class' : 'form-control'})   
        self.fields['unit'].widget.attrs.update({'class' : 'form-control'})        
