'''imports'''
from django.db import models

class Teacher(models.Model):
    '''TEACHER model definition'''
    login = models.CharField(max_length=7, unique=True, null=False)
    password = models.TextField(default="password", null=False)
    degree = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=25, null=False)
    surname = models.CharField(max_length=700, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.login + ', ' + self.name + ' ' + self.surname

    def get_subjects(self):
        return self.subjects.all()

class Subject(models.Model):
    '''SUBJECT model definition'''
    subject_code = models.CharField(max_length=20, null=False, unique=True)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=2000, null=False)
    min_points = models.IntegerField(null=False)
    created_at = models.DateField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, related_name='subjects', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.subject_code

class Student(models.Model):
    '''STUDENT model definition'''
    login = models.CharField(max_length=7, unique=True, null=False)
    password = models.TextField(default="password", null=False)
    degree = models.CharField(max_length=100, null=True, blank=False)
    name = models.CharField(max_length=25, null=False)
    surname = models.CharField(max_length=700, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(null=False)
    subject = models.ForeignKey(Subject, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.login
    
    def get_subject_id(self):
        return self.subject.id
