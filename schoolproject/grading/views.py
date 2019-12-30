'''imports'''
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Subject, Teacher, Student
from .forms import TeacherLoginForm, StudentLoginForm, AddPointsToStudentForm

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
    if request.method == 'POST':
        form = AddPointsToStudentForm(request.POST)
        if form.is_valid():
            stud = get_object_or_404(Student, login=form.cleaned_data['login'])
            new_points = stud.points + form.cleaned_data['points']
            Student.objects.filter(id=stud.id).update(points=new_points)
    else:
        form = AddPointsToStudentForm()
    return render(request, 'grading/teacher.html', {'teacher' : get_object_or_404(Teacher, id=teacher_id), 'form' : form})

def student_login(request):
    '''Login page for students'''
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            stud = get_object_or_404(Student, login=form.cleaned_data['login'])

            if stud.password == form.cleaned_data['password']:
                return HttpResponseRedirect('/student/'+str(stud.id))
            else: return HttpResponseRedirect('/student_login/')
    else:
        form = StudentLoginForm()
    return render(request, 'grading/student_login.html', {'form':form})

def teacher_login(request):
    '''Login page for students'''
    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            teach = get_object_or_404(Teacher, login=form.cleaned_data['login'])
            if teach.password == form.cleaned_data['password']:
                return HttpResponseRedirect('/teacher/'+str(teach.id))
            else: return HttpResponseRedirect('/teacher_login/')
    else:
        form = TeacherLoginForm()
    return render(request, 'grading/teacher_login.html', {'form':form})
