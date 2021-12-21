from django import forms
from infoapp import models

#creating student model forms
class StudentModelForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    phnumber = forms.IntegerField()
    address = forms.CharField(max_length=200)

#class meta:
#    model = Student
#    Fields = '__all_'
