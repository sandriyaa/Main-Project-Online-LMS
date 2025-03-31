"""
URL configuration for Lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login,name='login'),
    path('home/', views.home,name="home"),
    path('master_home/', views.master_home,name="master_home"),
    path('about/', views.about,name="about"),

    path('student_register/', views.student_register,name='student_register'),
    path('student_list/', views.student_list,name="student_list"),
    path('teacher_register/', views.teacher_register,name="teacher_register"),
    path('teachers_list/', views.teachers_list,name="teachers_list"),
    path('teacher_home/', views.teacher_home,name="teacher_home"),
    path('student_home/', views.student_home,name="student_home"),
    path('login_status/', views.login_status,name="login_status"),

    path('subject/', views.subject,name="subject"),
    path('edit_subject/', views.edit_subject,name="edit_subject"),
    path('delete_subject/', views.delete_subject,name="delete_subject"),

    path('category/', views.category,name="category"),
    path('edit_category/', views.edit_category,name="edit_category"),
    path('delete_category/', views.delete_category,name="delete_category"),

    path('course/', views.course,name="course"),
    path('course_list/', views.course_list,name="course_list"),
    path('edit_course/', views.edit_course,name="edit_course"),
    path('delete_course/', views.delete_course,name="delete_course"),

    path('batch/', views.batch,name="batch"),
    path('batch_list/', views.batch_list,name="batch_list"),
    path('batch_history/', views.batch_history,name="batch_history"),
    path('edit_batch/', views.edit_batch,name="edit_batch"),
    path('delete_batch/', views.delete_batch,name="delete_batch"),

    path('video/', views.video,name="video"),
    path('edit_video/', views.edit_video,name="edit_video"),
    path('delete_video/', views.delete_video,name="delete_video"),
    path('lecture_notes/', views.lecture_notes,name="lecture_notes"),

    path('assignment/', views.assignment,name="assignment"),
    path('assignment_list/', views.assignment_list,name="assignment_list"),
    path('edit_assignment/', views.edit_assignment,name="edit_assignment"),
    path('delete_assignment/', views.delete_assignment,name="delete_assignment"),

    path('exam/', views.exam,name="exam"),
    path('exam_list/', views.exam_list,name="exam_list"),
    path('edit_exam/', views.edit_exam,name="edit_exam"),
    path('exam_details/', views.exam_details,name="exam_details"),

    path('questions/', views.questions,name="questions"),
    path('edit_question/', views.edit_question,name="edit_question"),
    

    path('batches/', views.batches,name="batches"),
    path('join_batch/', views.join_batch,name="join_batch"),
    path('my_course/', views.my_course,name="my_course"),
    path('video_list/', views.video_list,name="video_list"),
    path('video_play/', views.video_play,name="video_play"),
    path('chat/', views.chat,name="chat"),
    path('doubt/', views.doubt,name="doubt"),
    path('active_exam/', views.active_exam,name="active_exam"),
    path('submission/', views.submission,name="submission"),
    path('batch_assignment/', views.batch_assignment,name="batch_assignment"),
    path('batch_exams/', views.batch_exams,name="batch_exams"),
    path('exam_batches/', views.exam_batches,name="exam_batches"),
    path('assessment/', views.assessment,name="assessment"),
    path('assessment_history/', views.assessment_history,name="assessment_history"),

    path('attend_exam/', views.attend_exam,name="attend_exam"),
    path('exam_history/', views.exam_history,name="exam_history"),
    path('exam_results/', views.exam_results,name="exam_results"),
    path('my_result/', views.my_result,name="my_result"),
    path('student_answer/', views.student_answer,name="student_answer"),

    path('progress/', views.progress,name="progress"),
    path('batch_students/', views.batch_students,name="batch_students"),
    path('enrollments/', views.enrollments,name="enrollments"),
    path('progress_report/', views.progress_report,name="progress_report"),
    path('active_batch/', views.active_batch,name="active_batch"),
    path('active_assignment/', views.active_assignment,name="active_assignment"),
    path('course_details/', views.course_details,name="course_details"),
    path('certificate/', views.certificate,name="certificate"),
    path('certificate_pdf/', views.certificate_pdf,name="certificate_pdf"),
    path('feedback/', views.feedback,name="feedback"),
    path('profile/', views.profile,name="profile"),
    path('change_password/', views.change_password,name="change_password"),
    path('receipt/', views.receipt,name="receipt"),

    
    path('search_course/', views.search_course,name="search_course"),
    path('search_course_text/', views.search_course_text,name="search_course_text"),
    path('search_teacher/', views.search_teacher,name="search_teacher"),
    path('search_student/', views.search_student,name="search_student"),
    path('search_lesson/', views.search_lesson,name="search_lesson"),
    path('search_batch/', views.search_batch,name="search_batch"),
    path('search_assignment/', views.search_assignment,name="search_assignment"),
    path('search_submission/', views.search_submission,name="search_submission"),
    path('search_result/', views.search_result,name="search_result"),
    path('search_enrollment/', views.search_enrollment,name="search_enrollment"),

    path('chat_user/', views.chat_user,name="chat_user"),
    path('chat_teacher/', views.chat_teacher,name="chat_teacher"),

    path('display_teacher/', views.display_teacher,name="display_teacher"),
    path('ed_teacher/', views.ed_teacher,name="ed_teacher"),
    path('sign_out/', views.sign_out,name="sign_out"),
    path('check_username/', views.check_username,name="check_username"),
]
