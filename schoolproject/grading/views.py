from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("index.html")
def subject(request):
    return HttpResponse("subject.html")
def subject_details(request, subject_id):
    return HttpResponse("subject_detail.html")
def student(request, student_id):
    return HttpResponse("student.html")
def teacher(request, teacher_id):
    return HttpResponse("teacher.html")
def student_login(request):
    return HttpResponse("student_login.html")
def teacher_login(request):
    return HttpResponse("teacher_login.html")