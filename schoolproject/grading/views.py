'''imports'''
from django.shortcuts import render, get_object_or_404
from .models import Subject, Teacher, Student

def index(request):
    '''home page view(index.html)'''
    return render(request, 'grading/index.html')

def subject(request):
    '''View on all existing subjects'''
    return render(request, 'grading/subject.html', {'all_subject_list' : Subject.objects.all})

def subject_details(request, subject_id):
    '''View on one specific subject'''
    return render(request, 'grading/subject_details.html', {'subject' : get_object_or_404(Subject, id=subject_id)})

def student(request, student_id):
    '''View on one specific student -> opens after student login'''
    return render(request, 'grading/student.html', {'student' : get_object_or_404(Student, id=student_id)})

def teacher(request, teacher_id):
    '''View on one specific teacher -> opens after teacher login'''
    return render(request, 'grading/teacher.html', {'teacher' : get_object_or_404(Teacher, id=teacher_id)})

def student_login(request):
    '''Login page for students'''
    return render(request, 'grading/student_login.html')

def teacher_login(request):
    '''Login page for teachers'''
    return render(request, 'grading/teacher_login.html')