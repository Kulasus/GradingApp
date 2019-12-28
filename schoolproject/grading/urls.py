'''imports'''
from django.urls import path
from . import views

app_name = 'eshop'
urlpatterns = [
    #mainviews
    path('', views.index, name='index'),
    path('subject/', views.subject, name="subject"),
    path('subject/<int:subject_id>', views.subject_details, name="subject_details"),
    path('student/<int:student_id>', views.student, name="student"),
    path('teacher/<int:teacher_id>', views.teacher, name="teacher"),
    #logins
    path('login/student/', views.student_login, name="student_login"),
    path('login/teacher/', views.teacher_login, name="teacher_login")
]