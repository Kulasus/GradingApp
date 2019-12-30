'''imports'''
from django import forms

class TeacherLoginForm(forms.Form):
    '''Login for Teacher'''
    login = forms.CharField(label="Login", max_length=7)
    password = forms.CharField(label="Password", max_length=100)

class StudentLoginForm(forms.Form):
    '''Login for Student'''
    login = forms.CharField(label="Login", max_length=7)
    password = forms.CharField(label="Password", max_length=100)

class AddPointsToStudentForm(forms.Form):
    '''Form for adding points to students'''
    login = forms.CharField(label="Login", max_length=7)
    points = forms.IntegerField(label="Points")
