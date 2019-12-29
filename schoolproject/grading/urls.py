'''imports'''
from django.urls import path
from . import views

app_name = 'grading'
urlpatterns = [
    #mainviews
    path('', views.index, name='index'),
    path('subject/', views.subject, name="subject"),
    path('subject/<int:subject_id>', views.subject_details, name="subject_details"),
    path('student/<int:student_id>', views.student, name="student"),
    path('teacher/<int:teacher_id>', views.teacher, name="teacher"),
    #logins
    path('student_login/', views.student_login, name="student_login"),
    path('teacher_login/', views.teacher_login, name="teacher_login")
]
