from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
import json
from datetime import date,datetime,timedelta,time,timezone
from django.db.models import Q,Max,ExpressionWrapper,Count,Sum,F,Case,When,BooleanField,OuterRef,Exists,IntegerField,Prefetch,DateField,Func,CharField,Value,FloatField,Subquery
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models.functions import Concat,Cast,ExtractMonth,ExtractYear
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.templatetags.static import static
from django.utils.text import Truncator

def about(request):
    data = Feedback.objects.select_related('student')
    return render(request,'about.html',{'data':data})

def home(request):
    if 'login_id' in request.session:
        user = request.session['login_id']
        if 'master' in request.session:
            return redirect('/master_home/')
        data = Login.objects.get(login_id=user)
        if data.user_type == 'Teacher':
            use = Teacher_register.objects.get(login_id=user)
            request.session['teacher'] = use.tr_id
            return redirect('/teacher_home/')
        elif data.user_type == 'Student':
            hos = Student_register.objects.get(login_id=user)
            request.session['student'] = hos.sr_id
            return redirect('/student_home/')
        else:
            return redirect('/home/')  
    else:
        data = Feedback.objects.select_related('student')
        return render(request,'index.html',{'data':data})

def login(request):
    if not request.session.keys():
        if request.method == 'POST':
            username=request.POST.get("username")
            password=request.POST.get("password")
            obj=authenticate(username=username,password=password)
            if obj is not None:
                if obj.is_superuser == 1:
                    request.session['login_id'] = obj.id
                    request.session['master'] = obj.id
                    return redirect('/home/')
                else:
                    messages.success(request, 'Invalid Username Or Password')
                    return redirect('/login/')
            else:
                try:
                    data = Login.objects.get(username=username,password=password)
                    if data.status == True:
                        request.session['login_id'] = data.login_id
                        return redirect('/home/')
                    else:
                        messages.success(request,'Admin denied your access')
                        return redirect('/login/')
                except Exception:
                    messages.success(request, 'Invalid Username Or Password')
                    return redirect('/login/')
        else:
            return render(request,'login.html')
    return redirect('/home')

def master_home(request):
    if 'master' in request.session:
        return render(request,'master/index.html')
    else:
        return redirect('/home/')

def teacher_home(request):
    if 'teacher' in request.session:
        return render(request,'teacher/index.html')
    else:
        return redirect('/home/')

def student_home(request):
    if 'student' in request.session:
        data = Feedback.objects.select_related('student')
        return render(request,'student/index.html',{'data':data})
    else:
        return redirect('/home/')  

def teacher_register(request):
    if request.method == 'POST':
        username=request.POST['username']
        if Login.objects.filter(username=username).exists() or User.objects.filter(username=username, is_superuser=True).exists():
            messages.success(request, 'This Username is already Exist.')
            return redirect('/teacher_register/')
        else:
            ob = Login()
            ob.username = request.POST['username']
            ob.password = request.POST['password']
            ob.user_type = 'Teacher'
            ob.save()

            d = Login.objects.get(username=request.POST['username'])

            obj = Teacher_register()
            obj.name = request.POST['name']
            obj.email = request.POST['email']
            obj.qualification = request.POST['qualification']
            obj.experience = request.POST['experience']
            obj.contact_number = request.POST['contact_number']
            obj.address = request.POST['address']
            obj.subject_id = request.POST['subject_id']
            obj.login = d
            if 'image' in request.FILES:
                im=request.FILES['image']
                ob = FileSystemStorage()
                fl = ob.save(im.name,im)

                obj.image = ob.url(fl)
            obj.save()
            messages.success(request, 'Registered successfully.')
            return redirect('/teacher_register/')
    else:
        sub = Subject.objects.all()
        return render(request,'master/teacher_register.html',{'sub':sub})
    
def teachers_list(request):
    if 'master' in request.session:
        data = Teacher_register.objects.select_related('login','subject')
        sub = Subject.objects.all()
        return render(request,'master/teachers_list.html',{'data':data,'sub':sub})
    else:
        return redirect('/home/')
    
def student_register(request):
    if request.method == 'POST':
        username=request.POST['username']
        if Login.objects.filter(username=username).exists() or User.objects.filter(username=username, is_superuser=True).exists():
            messages.success(request, 'This Username is already Exist.')
            return redirect('/student_register/')
        else:
            ob = Login()
            ob.username = request.POST['username']
            ob.password = request.POST['password']
            ob.user_type = 'Student'
            ob.save()

            d = Login.objects.get(username=request.POST['username'])

            obj = Student_register()
            obj.name = request.POST['name']
            obj.email = request.POST['email']
            obj.contact_number = request.POST['contact_number']
            obj.address = request.POST['address']
            obj.login = d
            if 'image' in request.FILES:
                im=request.FILES['image']
                ob = FileSystemStorage()
                fl = ob.save(im.name,im)
                
                obj.image = ob.url(fl)
            obj.save()
            messages.success(request, 'Registered successfully.')
            return redirect('/student_register/')
    else:
        return render(request,'student_register.html')
    
def student_list(request):
    data = Student_register.objects.select_related('login').order_by('-sr_id')
    bat = Batch.objects.filter(status=True).select_related('course')
    context = {'data':data,'bat':bat}
    if 'master' in request.session:
        return render(request,'master/student_list.html',context)
    elif 'teacher' in request.session:
        return render(request,'teacher/student_list.html',context)
    else:
        return redirect('/home/')
    
def login_status(request):
    if 'master' in request.session:
        data = Login.objects.get(login_id=request.GET['login_id'])
        data.status = request.GET['status']
        data.save()
        messages.success(request, 'Access updated successfully')
        return redirect('/student_list/')
    else:
        return redirect('/home/')

def subject(request):
    if 'master' in request.session:
        if request.method == 'POST':
            obj = Subject()
            obj.subject = request.POST['subject']
            obj.save()
            messages.success(request, 'Added successfully.')
            return redirect('/subject/')
        else:
            data = Subject.objects.all()
            return render(request,'master/subject.html',{'data':data})
    else:
        return redirect('/home/')
    
def edit_subject(request):
    if 'master' in request.session:
        if request.method == 'POST':
            obj = Subject.objects.get(s_id=request.POST['s_id'])
            obj.subject = request.POST['subject']
            obj.save()
            messages.success(request, 'Updated successfully.')
            return redirect('/subject/')
        elif 's_id' in request.GET:
            data = Subject.objects.get(s_id=request.GET['s_id'])
            return render(request,'master/edit_subject.html',{'data':data})
        else:
            return redirect('/subject/')
    else:
        return redirect('/home/')

def delete_subject(request):
    if 'master' in request.session:
        data = Subject.objects.get(s_id=request.GET['s_id'])
        data.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('/subject/')
    else:
        return redirect('/home/')
    
def category(request):
    if 'master' in request.session:
        if request.method == 'POST':
            obj = Category()
            obj.course_category = request.POST['course_category']
            obj.save()
            messages.success(request, 'Added successfully.')
            return redirect('/category/')
        else:
            data = Category.objects.all()
            return render(request,'master/category.html',{'data':data})
    else:
        return redirect('/home/')
    
def edit_category(request):
    if 'master' in request.session:
        if request.method == 'POST':
            obj = Category.objects.get(ct_id=request.POST['ct_id'])
            obj.course_category = request.POST['course_category']
            obj.save()
            messages.success(request, 'Updated successfully.')
            return redirect('/category/')
        elif 'ct_id' in request.GET:
            data = Category.objects.get(ct_id=request.GET['ct_id'])
            return render(request,'master/edit_category.html',{'data':data})
        else:
            return redirect('/category/')
    else:
        return redirect('/home/')

def delete_category(request):
    if 'master' in request.session:
        data = Category.objects.get(ct_id=request.GET['ct_id'])
        data.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('/category/')
    else:
        return redirect('/home/')
    
def course(request):
    if 'master' in request.session:
        if request.method == 'POST':
            obj = Course()
            obj.course_name = request.POST['course_name']
            obj.fees = request.POST['fees']
            obj.category_id = request.POST['category_id']
            obj.description = request.POST['description']
            if request.POST['certificate_course'] == 'Yes':
                obj.certificate_course = True
            else:
                obj.certificate_course = False
            if 'image' in request.FILES:
                im=request.FILES['image']
                ob = FileSystemStorage()
                fl = ob.save(im.name,im)

                obj.image = ob.url(fl)
            obj.save()
            subject_id = request.POST.getlist('subject_id')
            obj.subjects.add(*subject_id)  
            messages.success(request, 'Added successfully.')
            return redirect('/course/')
        else:
            data = Subject.objects.all()
            cat = Category.objects.all()
            return render(request,'master/course.html',{'sub':data,'cat':cat})
    else:
        return redirect('/home/')
    
def edit_course(request):
    if 'master' in request.session:
        if request.method == 'POST':
            obj = Course.objects.get(c_id=request.POST['c_id'])
            obj.course_name = request.POST['course_name']
            obj.fees = request.POST['fees']
            obj.category_id = request.POST['category_id']
            obj.description = request.POST['description']
            if request.POST['certificate_course'] == 'Yes':
                obj.certificate_course = True
            else:
                obj.certificate_course = False

            if 'image' in request.FILES:
                im=request.FILES['image']
                ob = FileSystemStorage()
                fl = ob.save(im.name,im)

                obj.image = ob.url(fl)
            obj.save()
            subject_id = request.POST.getlist('subject_id')
            obj.subjects.set(subject_id)  
            messages.success(request, 'Course updated successfully.')
            return redirect('/course_list/')
        else:
            data = Course.objects.get(c_id=request.GET.get('c_id'))
            sub = Subject.objects.all()
            ids = data.subjects.values_list('s_id', flat=True) 
            cat = Category.objects.all()
            return render(request, 'master/edit_course.html', {'sub': sub,'data': data,'ids': ids,'cat': cat})
    else:
        return redirect('/home/')

def course_list(request):
    data = Course.objects.all().order_by('category_id').order_by('-c_id')
    cat = Category.objects.all()
    if 'master' in request.session:
        return render(request,'master/course_list.html',{'data':data})
    elif 'student' in request.session:
        return render(request,'student/course_list.html',{'data':data,'cat':cat})
    else:
        return render(request,'course_list.html',{'data':data,'cat':cat})

def delete_course(request):
    if 'master' in request.session:
        data = Course.objects.get(c_id=request.GET['c_id'])
        data.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('/course_list/')
    else:
        return redirect('/home/')
    
def batch(request):
    if 'master' in request.session:
        if request.method == 'POST':
            obj = Batch()
            obj.title = request.POST['title']
            obj.closing_date = request.POST['closing_date']
            obj.start_date = request.POST['start_date']
            obj.end_date = request.POST['end_date']
            obj.course_id = request.POST['course_id']
            obj.save()
            teacher_id = request.POST.getlist('teacher_id')
            obj.teacher.add(*teacher_id)  
            messages.success(request, 'Added successfully.')
            return redirect('/batch/')
        else:
            data = Course.objects.all()
            return render(request,'master/batch.html',{'cos':data})
    else:
        return redirect('/home/')
    
def batch_list(request):
    if 'master' in request.session:
        data = Batch.objects.filter(status=False).select_related('course').order_by('-b_id')
        return render(request,'master/batch_list.html',{'data':data})
    elif 'teacher' in request.session:
        data = Batch.objects.filter(end_date__gte=date.today(),teacher=request.session['teacher']).select_related('course').order_by('-b_id')
        return render(request,'teacher/batch_list.html',{'data':data})
    else:
        return redirect('/home/')

def enrollments(request):
    if 'master' in request.session:
        data = Enrollment.objects.select_related('batch','student').order_by('e_id')
        bat = Batch.objects.filter(status=True).select_related('course').order_by('-b_id')
        return render(request,'master/enrollments.html',{'data':data,'bat':bat})
    elif 'student' in request.session:
        data = Enrollment.objects.filter(student_id=request.session['student']).select_related('batch','student').order_by('e_id')
        return render(request,'student/enrollments.html',{'data':data})
    else:
        return redirect('/home/')

def batches(request):
    if 'student' in request.session:
        if 'course_id' in request.GET:
            data = Batch.objects.filter(course_id=request.GET.get('course_id'),closing_date__gte=date.today(),status=True).annotate(
                exist=Case(When(Exists(Enrollment.objects.filter(Q(batch_id=OuterRef('b_id'))&Q(student_id=request.session['student']))),
                        then=True),
                        default=False,
                        output_field=BooleanField()
                )
            ).select_related('course').order_by('b_id')
            return render(request,'student/batches.html',{'data':data})
    elif 'master' in request.session:
        data = Batch.objects.filter(end_date__gte=date.today(),status=True).select_related('course').order_by('b_id')
        return render(request,'master/batches.html',{'data':data,'s':'a'})
    else:
        if 'course_id' in request.GET:
            data = Batch.objects.filter(course_id=request.GET.get('course_id'),closing_date__gte=date.today(),status=True).select_related('course').order_by('-b_id')
            return render(request,'batches.html',{'data':data})
        else:
            return redirect('/home/')
    
def course_details(request):
    if 'student' in request.session:
        if 'b_id' in request.GET:
            data = get_object_or_404(
                    Batch.objects.annotate(
                        exist=Exists(Enrollment.objects.filter(batch=OuterRef("pk"), student_id=request.session['student']))
                    ),
                    pk=request.GET.get('b_id')
                )         
            return render(request,'student/course_details.html',{'data':data})
    else:
        if 'b_id' in request.GET:
            data = Batch.objects.get(pk=request.GET.get('b_id'))         
            return render(request,'course_details.html',{'data':data})
        return redirect('/home/')

def batch_history(request):
    if 'master' in request.session:
        data = Batch.objects.filter(end_date__lt=date.today(),status=True).select_related('course').order_by('-b_id')
        return render(request,'master/batches.html',{'data':data,'s':'h'})
    elif 'teacher' in request.session:
        data = Batch.objects.filter(end_date__lt=date.today(),teacher=request.session['teacher']).select_related('course').order_by('-b_id')
        return render(request,'teacher/batch_history.html',{'data':data})
    elif 'student' in request.session:
        data = Enrollment.objects.filter(batch__end_date__lt=date.today(),student_id=request.session['student']).annotate(
            cc = F('batch__course__certificate_course')
        ).select_related('batch','student').order_by('-e_id')
        return render(request,'student/batch_history.html',{'data':data})
    else:
        return redirect('/home/')
    
def certificate(request):
    if 'student' in request.session:
        data = Enrollment.objects.annotate(
            issue_date=ExpressionWrapper(F('batch__end_date') + timedelta(days=1), output_field=DateField())
        ).get(e_id=request.GET.get('e_id'))
        return render(request,'student/certificate.html',{'data':data})
    else:
        return redirect('/home/')
    
def certificate_pdf(request):
    data = Enrollment.objects.annotate(
            issue_date=ExpressionWrapper(F('batch__end_date') + timedelta(days=1), output_field=DateField())
        ).get(e_id=request.GET.get('e_id'))
    id = request.GET['e_id']
    response = HttpResponse (content_type="application/pdf")
    response['Content-Disposition'] = f'attachment; filename="certificate_{id}.pdf"'

    domain = "http://localhost:8000"
    logo_url = domain + static('user/img/download.png')
    signature_url = domain + static('user/img/gett.jpg')

    html = render_to_string('student/certificate_pdf.html', {'data': data,'logo_url': logo_url,'signature_url': signature_url,})

    pisa_status = pisa.CreatePDF(html, dest=response) 

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')   
    return response
    

 
def assessment(request):
    if 'master' in request.session:
        data = Batch.objects.filter(end_date__gte=date.today()).select_related('course').order_by('-b_id')
        return render(request,'master/assessment.html',{'data':data})
    else:
        return redirect('/home/')
    
def assessment_history(request):
    if 'master' in request.session:
        data = Batch.objects.filter(end_date__lt=date.today()).select_related('course').order_by('-b_id')
        return render(request,'master/assessment.html',{'data':data})
    else:
        return redirect('/home/')
    
def join_batch(request):
    if 'student' in request.session:
        if request.method == 'POST':
            obj = Enrollment()
            obj.batch_id = request.POST['b_id']
            obj.student_id = request.session['student']
            obj.amount = request.POST['amount']
            obj.save()
            messages.success(request, 'Submitted successfully.')
            return redirect('/my_course/')
        elif 'b_id' in request.GET:
            data = Batch.objects.get(b_id=request.GET['b_id'])
            return render(request,'student/join_batch.html',{'data':data})
        else:
            return redirect('/home/')
    else:
        return redirect('/home/')
    
def my_course(request):
    if 'student' in request.session:
        data = Enrollment.objects.filter(student_id=request.session['student'],batch__end_date__gte=date.today()).select_related('student','batch')
        return render(request,'student/my_course.html',{'data':data})
    else:
        return redirect('/home/')

def edit_batch(request):
    if 'master' in request.session:
        if request.method == 'POST':
            obj = Batch.objects.get(b_id=request.POST['b_id'])
            obj.title = request.POST['title']
            obj.closing_date = request.POST['closing_date']
            obj.start_date = request.POST['start_date']
            obj.end_date = request.POST['end_date']
            obj.course_id = request.POST['course_id']
            obj.save()
            teacher_id = request.POST.getlist('teacher_id')
            obj.teacher.set(teacher_id)  
            messages.success(request, 'Batch updated successfully.')
            return redirect('/batch/')
        else:
            data = Batch.objects.get(b_id=request.GET.get('b_id'))
            sub = Course.objects.all()
            tr = Teacher_register.objects.filter(subject__course__c_id=data.course_id).select_related('login','subject')
            ids = data.teacher.values_list('tr_id', flat=True) 
            return render(request, 'master/edit_batch.html', {'cos': sub,'data': data,'ids': ids,'tr':tr})
    else:
        return redirect('/home/')

def delete_batch(request):
    if 'master' in request.session:
        data = Batch.objects.get(b_id=request.GET['b_id'])
        data.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('/batch/')
    else:
        return redirect('/home/')
    
def video(request):
    if 'teacher' in request.session:
        if request.method == 'POST':
            sub = Teacher_register.objects.get(tr_id=request.session['teacher'])
            obj = Lesson()
            obj.title = request.POST['title']
            obj.subject_id = sub.subject_id
            if 'video' in request.FILES:
                im=request.FILES['video']
                ob = FileSystemStorage()
                fl = ob.save(im.name,im)

                obj.video = ob.url(fl)
            obj.teacher_id = request.session['teacher'] 
            obj.save()
            messages.success(request, 'Uploaded successfully.')
            return redirect('/video/')
        sub = Subject.objects.all()
        data = Lesson.objects.filter(teacher=request.session['teacher']).prefetch_related('lecture_notes_set').order_by('-l_id')
        return render(request,'teacher/video.html',{'data':data,'sub':sub})
    elif 'student' in request.session:
        if 'b_id' in request.GET:
            b_id = request.GET.get('b_id')
            bt = Batch.objects.filter(b_id=b_id).values_list('teacher')
            first_video_subquery = Lesson.objects.filter(subject_id=OuterRef('subject_id')).order_by('l_id').values('video')[:1]

            data = (
                Lesson.objects.filter(teacher_id__in=bt)
                .values('subject__subject')  
                .annotate(
                    video_count=Count('l_id'),  
                    thumb_nail=Subquery(first_video_subquery),
                    teacher_id = F('teacher_id'),
                    teacher = F('teacher__name'),
                )
                .order_by('-video_count') 
            )
            return render(request,'student/video.html',{'data':data})
        else:
            return redirect('/home/')
    elif 'master' in request.session:
        data = Teacher_register.objects.annotate(nov = Count('lessons__l_id')).select_related('login','subject')
        return render(request,'master/video.html',{'data':data})
    return redirect('/home/')

def video_list(request):
    if 'teacher_id' in request.GET:
        if 'student' in request.session: 
            data = Lesson.objects.filter(teacher_id=request.GET.get('teacher_id')).select_related('subject','teacher')
            return render(request,'student/video_list.html',{'data':data})
        elif 'master' in request.session: 
            data = Lesson.objects.filter(teacher_id=request.GET.get('teacher_id')).prefetch_related('lecture_notes_set')
            return render(request,'master/video_list.html',{'data':data})
        else:
            return redirect('/home/')
    return redirect('/home/')

def video_play(request):
    if 'student' in request.session:
        if 'l_id' in request.GET:
            l_id = request.GET.get('l_id')

            data = get_object_or_404(
                Lesson.objects.prefetch_related(
                    Prefetch(
                        'lecture_notes_set',
                        queryset=Lecture_notes.objects.all(),
                        to_attr='notes'
                    ),
                    Prefetch(
                        'teacher__lessons',
                        queryset=Lesson.objects.exclude(pk=l_id),
                        to_attr='other_lessons'
                    )
                ).select_related('teacher', 'subject'),
                pk=l_id
            )
            print(data.teacher.other_lessons)
            return render(request,'student/video_play.html',{'data':data})
        else:
            return redirect('/home/')
    return redirect('/home/')

def edit_video(request):
    if 'teacher' in request.session:
        if request.method == 'POST':
            obj = Lesson.objects.get(l_id=request.POST.get('l_id'))
            obj.title = request.POST['title']
            obj.subject_id = request.POST['subject_id']
            if 'video' in request.FILES:
                im=request.FILES['video']
                ob = FileSystemStorage()
                fl = ob.save(im.name,im)

                obj.video = ob.url(fl)
            obj.save()
            messages.success(request, 'Submitted successfully.')
            return redirect('/video/')
        sub = Subject.objects.all()
        data = Lesson.objects.get(l_id=request.GET.get('l_id'))
        return render(request,'teacher/edit_video.html',{'data':data,'sub':sub})
    return redirect('/home/')

def delete_video(request):
    if 'teacher' in request.session:
        data = Lesson.objects.get(l_id=request.GET['l_id'])
        data.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('/video/')
    else:
        return redirect('/home/')

def lecture_notes(request):
    if 'teacher' in request.session:
        if request.method == 'POST':
            obj = Lecture_notes()
            obj.video_id = request.POST['video_id']
            if 'note' in request.FILES:
                im=request.FILES['note']
                ob = FileSystemStorage()
                fl = ob.save(im.name,im)

                obj.note = ob.url(fl)
            obj.save()
            messages.success(request, 'Submitted successfully.')
            return redirect('/lecture_notes?l_id='+request.POST['video_id'])
        data = Lesson.objects.get(l_id=request.GET.get('l_id'))
        v = data.lecture_notes_set.all()
        for i in v:
            print(i.note)

        return render(request,'teacher/lecture_notes.html',{'data':data})
    return redirect('/home/')

def assignment(request):
    if 'teacher' in request.session:
        if request.method == 'POST':
            obj = Assignment()
            obj.title = request.POST['title']
            obj.description = request.POST['description']
            obj.due_date = request.POST['due_date']
            obj.total_mark = request.POST['total_mark']
            obj.teacher_id = request.session['teacher']
            obj.save()  
            batch_id = request.POST.getlist('batch_id')
            obj.batch.add(*batch_id)
            messages.success(request, 'Added successfully.')
            return redirect('/assignment/')
        else:
            bat = Batch.objects.filter(end_date__gte=date.today(),teacher=request.session['teacher']).select_related('course')
            return render(request,'teacher/assignment.html',{'bat':bat})
    elif 'student' in request.session:
        if 'b_id' in request.GET:
            data = Assignment.objects.filter(batch=request.GET.get('b_id'),status=True).annotate(
                        exist=Case(When(Exists(Submission.objects.filter(Q(student_id=request.session['student'])&Q(assignment_id=OuterRef('a_id')))),
                        then=True),
                        default=False,
                        output_field=BooleanField())
                    ).select_related('teacher').order_by('-a_id')
            return render(request,'student/assignment.html',{'data':data})  
        else:
            return redirect('/my_course/')
    else:
        return redirect('/home/')

def assignment_list(request):
    if 'master' in request.session:
        if 'batch_id' in request.GET:
            data = Assignment.objects.filter(batch=request.GET.get('batch_id')).select_related('teacher').order_by('-a_id')
            return render(request,'master/assignment_list.html',{'data':data})
        else:
            return redirect('/assessment/')
    elif 'teacher' in request.session:
        if 'batch_id' in request.GET:
            data = Assignment.objects.filter(teacher_id=request.session['teacher'],batch=request.GET.get('batch_id')).select_related('teacher').order_by('-a_id')
        else:
            data = Assignment.objects.filter(teacher_id=request.session['teacher']).select_related('teacher').order_by('-a_id')
        return render(request,'teacher/assignment_list.html',{'data':data})
    else:
        return redirect('/home/')

def batch_assignment(request):
    if 'master' in request.session:
        data = Assignment.objects.filter(batch_id=request.GET.get('batch_id')).select_related('batch','teacher').order_by('-a_id')
        return render(request,'master/batch_assignment.html',{'data':data})
    elif 'teacher' in request.session:
        if 'b_id' and 'a_id' in request.GET:
            a_id = request.GET.get('a_id')
            b_id = request.GET.get('b_id')
            data = Submission.objects.filter(assignment_id=a_id,assignment__batch=b_id,assignment__teacher_id=request.session['teacher']).select_related('assignment','student').order_by('-s_id')
            return render(request,'teacher/submission.html',{'data':data})
        else:
            data = Assignment.objects.filter(teacher_id=request.session['teacher']).select_related('teacher').order_by('-a_id')
            return render(request,'teacher/batch_assignment.html',{'data':data})
    else:
        return redirect('/home/')
   
def submission(request):
    if 'student' in request.session:
        if request.method == 'POST':
            obj = Submission()
            if 'assignment_file' in request.FILES:
                im=request.FILES['assignment_file']
                ob = FileSystemStorage()
                fl = ob.save(im.name,im)

                obj.assignment_file = ob.url(fl)
            obj.assignment_id = request.POST['a_id']
            obj.student_id = request.session['student']
            obj.save()
            return redirect('/my_course/')
        else:
            if 'b_id' in request.GET:
                data = Submission.objects.filter(assignment__batch=request.GET.get('b_id'),student_id=request.session['student']).select_related('student','assignment')
                return render(request,'student/submission.html',{'data':data})
            else:
                return redirect('/my_course/')
    elif 'teacher' in request.session:
        if request.method == 'POST':
            obj = Submission.objects.get(s_id=request.POST.get('s_id'))
            obj.mark = request.POST['mark']
            obj.save()
            return redirect('/batch_assignment/')
        else:
            if 'b_id' in request.GET:
                data = Submission.objects.filter(assignment__batch=request.GET.get('b_id'),assignment__teacher_id=request.session['teacher']).select_related('student','assignment').order_by(F('mark').asc(nulls_first=True))
                return render(request,'teacher/submission.html',{'data':data})
            else:
                return redirect('/batch_assignment/')   
    elif 'master' in request.session:
        if 'b_id' in request.GET:
            data = Submission.objects.filter(assignment__batch=request.GET.get('b_id')).select_related('student','assignment').order_by('-s_id')
            return render(request,'master/submission.html',{'data':data})
        else:
            return redirect('/my_course/') 
    else:
        return redirect('/home/')
    
def edit_assignment(request):
    if 'teacher' in request.session:
        if request.method == 'POST':
            obj = Assignment.objects.get(a_id=request.POST['a_id'])
            obj.title = request.POST['title']
            obj.description = request.POST['description']
            obj.due_date = request.POST['due_date']
            obj.mark = request.POST['mark']
            obj.save() 
            batch_id = request.POST.getlist('batch_id')
            obj.batch.set(batch_id)
            messages.success(request, 'Updated successfully.')
            return redirect('/assignment/')
        else:
            bat = Batch.objects.filter(end_date__gte=date.today(),teacher=request.session['teacher']).select_related('course')
            data = Assignment.objects.get(a_id=request.GET['a_id'])
            ids = data.batch.values_list('b_id', flat=True) 
            return render(request,'teacher/edit_assignment.html',{'data':data,'bat':bat,'ids':ids})
    else:
        return redirect('/home/')

def delete_assignment(request):
    if 'teacher' in request.session:
        data = Assignment.objects.get(a_id=request.GET['a_id'])
        data.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('/assignment/')
    else:
        return redirect('/home/')

def exam(request):
    if 'teacher' in request.session:
        if request.method == 'POST':
            obj = Exam()
            obj.teacher_id = request.session['teacher']
            obj.title = request.POST['title']
            obj.topic = request.POST['topic']
            if request.POST['format'] == 'hour':
                obj.duration = float(request.POST['duration'])*60
            else:
                obj.duration = request.POST['duration']
            obj.save()
            batch_id = request.POST.getlist('batch_id')
            obj.batch.add(*batch_id)
            messages.success(request, 'Submitted successfully.')
            return redirect('/exam/')
        else:
            bat = Batch.objects.filter(teacher=request.session['teacher']).select_related('course')
            return render(request,'teacher/exam.html',{'bat':bat})
    elif 'student' in request.session:
        if request.method == 'POST':
            question_ids = request.POST.getlist('question_id')

            for q_id in question_ids:
                answer = request.POST.get('answer_'+q_id)
                print(request.POST.get('answer_'+q_id))
                if answer:  
                    Answers.objects.create(question_id=q_id, answer=answer,student_id=request.session['student'])

            return redirect('/exam_list/')
        else:
            return redirect('/home/')
    else:
        return redirect('/home/')

def edit_exam(request):
    if 'teacher' in request.session:
        if request.method == 'POST':
            obj = Exam.objects.get(e_id=request.POST.get('e_id'))
            obj.topic = request.POST['topic']
            obj.title = request.POST['title']
            if request.POST['format'] == 'hour':
                obj.duration = int(request.POST['duration'])*60
            else:
                obj.duration = request.POST['duration']
            obj.save()
            batch_id = request.POST.getlist('batch_id')
            obj.batch.set(*batch_id)
            messages.success(request, 'Submitted successfully.')
            return redirect('/exam_list/')
        elif 'e_id' in request.GET:            
            bat = Batch.objects.filter(teacher=request.session['teacher']).select_related('course')
            data = Exam.objects.get(e_id=request.GET.get('e_id'))
            ids = data.batch.values_list('b_id', flat=True)
            return render(request,'teacher/edit_exam.html',{'bat':bat,'data':data,'ids':ids})
        else:
            return redirect('/exam_list/')
    else:
        return redirect('/home/')

def exam_list(request):
    if 'teacher' in request.session:
        if 'b_id' in request.GET:
            data = Exam.objects.filter(teacher=request.session['teacher'],batch=request.GET.get('b_id')).annotate(
                    et = Case(
                        When(Q(duration__gt=59),
                             then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                             default=Concat(F('duration'), Value('m')),
                             output_field=CharField()
                    )
                ).select_related('teacher').order_by('-e_id')
        else:
            data = Exam.objects.filter(teacher=request.session['teacher']).annotate(
                    et = Case(
                        When(Q(duration__gt=59),
                             then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                             default=Concat(F('duration'), Value('m')),
                             output_field=CharField()
                    )
                ).select_related('teacher').order_by('-e_id')
        return render(request,'teacher/exam_list.html',{'data':data})
    if 'master' in request.session:
        if 'b_id' in request.GET:
            data = Exam.objects.filter(batch=request.GET.get('b_id')).annotate(
                    et = Case(
                        When(Q(duration__gt=59),
                             then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                             default=Concat(F('duration'), Value('m')),
                             output_field=CharField()
                    )
                ).select_related('teacher').order_by('-e_id')
            return render(request,'master/exam_list.html',{'data':data})
        else:
            return redirect('/assessment/')
    elif 'student' in request.session:
        if 'b_id' in request.GET:
            data = Exam.objects.filter(batch=request.GET.get('b_id'),status=True).annotate(
                        exist=Case(When(Exists(Answers.objects.filter(Q(student_id=request.session['student'])&Q(question__exam=OuterRef('e_id')))),
                        then=True),
                        default=False,
                        output_field=BooleanField())
                    ).select_related('teacher')
            print(data)
            return render(request,'student/exam_list.html',{'data':data})
        else:
            return redirect('/my_course/')
    else:
        return redirect('/home/')

def batch_exams(request):
    if 'teacher' in request.session:
        if 'b_id' in request.GET:
            data = Batch.objects.filter(pk=request.GET.get('b_id')).prefetch_related(
                    Prefetch('exam_set', queryset=Exam.objects.filter(teacher_id=request.session['teacher']).annotate(
                        et=Case(
                            When(Q(duration__gt=59), then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                            default=Concat(F('duration'), Value('m')),
                            output_field=CharField()
                        )
                    ))
                ).get(pk=request.GET.get('b_id'))
            return render(request,'teacher/batch_exams.html',{'data':data})
        else:
            return render('/exam_list/')
    if 'master' in request.session:
        if 'b_id' in request.GET:
            data = Batch.objects.filter(pk=request.GET.get('b_id')).prefetch_related(
                    Prefetch('exam_set', queryset=Exam.objects.annotate(
                        et=Case(
                            When(Q(duration__gt=59), then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                            default=Concat(F('duration'), Value('m')),
                            output_field=CharField()
                        )
                    ))
                ).get(pk=request.GET.get('b_id'))
            return render(request,'master/batch_exams.html',{'data':data})
        else:
            return render('/assessment/')
    else:
        return redirect('/home/')
    
def exam_results(request):
    if 'teacher' in request.session:
        if 'b_id' and 'e_id' in request.GET:
            exam = get_object_or_404(Exam.objects.annotate(
                    et = Case(
                        When(Q(duration__gt=59),
                             then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                             default=Concat(F('duration'), Value('m')),
                             output_field=CharField()
                    )),pk=request.GET.get('e_id'))
            data = (
            Student_register.objects
            .filter(answers__question__exam_id=request.GET.get('e_id'),enrollment__batch_id=request.GET.get('b_id'))  
            .annotate(
                total_marks=Sum(
                    Case(
                        When(
                            answers__answer=F('answers__question__answer'),  
                            then=1  
                        ),
                        default=0,
                        output_field=IntegerField()
                    )
                ),
                total_questions=Count('answers__question')
            )
            .values(
                'sr_id', 'name', 'image', 'total_marks', 'total_questions',
                'answers__question__exam_id'
            )
            )
            return render(request,'teacher/exam_results.html',{'data':data,'exam':exam})
        else:
            return render('/exam_list/')
    if 'master' in request.session:
        if 'b_id' and 'e_id' in request.GET:
            exam = get_object_or_404(Exam.objects.annotate(
                    et = Case(
                        When(Q(duration__gt=59),
                             then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                             default=Concat(F('duration'), Value('m')),
                             output_field=CharField()
                    )),pk=request.GET.get('e_id'))
            data = (
            Student_register.objects
            .filter(answers__question__exam_id=request.GET.get('e_id'),enrollment__batch_id=request.GET.get('b_id'))  
            .annotate(
                total_marks=Sum(
                    Case(
                        When(
                            answers__answer=F('answers__question__answer'),  
                            then=1  
                        ),
                        default=0,
                        output_field=IntegerField()
                    )
                ),
                total_questions=Count('answers__question')
            )
            .values(
                'sr_id', 'name', 'image', 'total_marks', 'total_questions',
                'answers__question__exam_id'
            )
            )
            return render(request,'master/exam_results.html',{'data':data,'exam':exam})
        else:
            return render('/assessment/')
    else:
        return redirect('/home/')

def student_answer(request):
    if 'e_id' in request.GET:
        student_id = request.GET.get('sr_id')
        exam_id = request.GET.get('e_id')
        stu = Student_register.objects.get(sr_id=student_id)
        exam = get_object_or_404(
        Exam.objects.filter(pk=exam_id,questions__answers__student_id=student_id)
            .annotate(
                no_of_questions=Count('questions'),
                total_mark=Sum(
                    Case(
                        When(
                            questions__answers__student_id=student_id,
                            questions__answers__answer=F('questions__answer'),
                            then=1
                        ),
                        default=0,
                        output_field=IntegerField()
                    )
                ),
                attended_questions = Count('questions__answers__answer'),
                wrong = F('attended_questions') - F('total_mark'),
                et = Case(
                        When(Q(duration__gt=59),
                             then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                             default=Concat(F('duration'), Value('m')),
                             output_field=CharField()
                    )
            )
            .prefetch_related(
                Prefetch(
                    'questions_set',
                    queryset=Questions.objects.prefetch_related(
                        Prefetch(
                            'answers_set',
                            queryset=Answers.objects.filter(student_id=student_id)
                        )
                    )
                )
            )
        )
        if 'teacher' in request.session:
            return render(request,'teacher/student_answer.html',{'exam':exam,'stu':stu})
        elif 'master' in request.session:
            return render(request,'master/student_answer.html',{'exam':exam,'stu':stu})
    else:
        return redirect('/exam_results/')

def exam_history(request):
    if 'student' in request.session:
        if 'b_id' in request.GET:
           
            data = Exam.objects.filter(
                    batch=request.GET.get('b_id'),
                    status=True,
                    questions__answers__student_id=request.session['student']
                ).distinct().select_related('teacher')
            
            return render(request,'student/exam_history.html',{'data':data})
        else:
            return redirect('/my_course/')
    else:
        return redirect('/home/')
    
def exam_batches(request):
    if 'teacher' in request.session:
        data = Exam.objects.filter(teacher_id=request.session['teacher']).annotate(
                    et = Case(
                        When(Q(duration__gt=59),
                             then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                             default=Concat(F('duration'), Value('m')),
                             output_field=CharField()
                    )
                ).select_related('teacher').order_by('-e_id')
        return render(request,'teacher/exam_batches.html',{'data':data})
    else:
        return redirect('/home/')
    
def my_result(request):
    if 'student' in request.session:
        if 'e_id' in request.GET:
            student_id = request.session['student']
            exam_id = request.GET.get('e_id')
            exam = get_object_or_404(
            Exam.objects.filter(pk=exam_id,questions__answers__student_id=student_id)
                .annotate(
                    no_of_questions=Count('questions'),
                    total_mark=Sum(
                        Case(
                            When(
                                questions__answers__answer=F('questions__answer'),
                                then=1
                            ),
                            default=0,
                            output_field=IntegerField()
                        )
                    ),
                    attended_questions = Count('questions__answers__answer'),
                    wrong = F('attended_questions') - F('total_mark'),
                )
                .prefetch_related(
                    Prefetch(
                        'questions_set',
                        queryset=Questions.objects.prefetch_related(
                            Prefetch(
                                'answers_set',
                                queryset=Answers.objects.filter(student_id=student_id)
                            )
                        )
                    )
                )
            )
            return render(request,'student/my_result.html',{'exam':exam})
    else:
        return redirect('/home/')  

def exam_details(request):
    if 'e_id' in request.GET:
        if 'teacher' in request.session:
            data = get_object_or_404(
                Exam.objects.annotate(
                    vt = Case(
                        When(Q(duration__gt=59),
                             then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                             default=Concat(F('duration'), Value('m')),
                             output_field=CharField()
                    )
                ).prefetch_related('questions_set'),
                pk=request.GET['e_id']
            )
            return render(request,'teacher/exam_details.html',{'data':data})
        elif 'master' in request.session:
            data = get_object_or_404(
                Exam.objects.annotate(
                    vt = Case(
                        When(Q(duration__gt=59),
                             then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                             default=Concat(F('duration'), Value('m')),
                             output_field=CharField()
                    )
                ).prefetch_related('questions_set'),
                pk=request.GET['e_id']
            )
            return render(request,'master/exam_details.html',{'data':data})
        else:
            return redirect('/home/')
    else:
        return redirect('/exam_list/')

def active_exam(request):
    if 'teacher' in request.session:
        if 'e_id' in request.GET:
            ex = Questions.objects.filter(exam_id=request.GET.get('e_id')).exists()
            if ex:
                obj = Exam.objects.get(e_id=request.GET.get('e_id'))
                obj.status = True
                obj.save()
                messages.success(request, 'Exam is active')
                return redirect('/exam_list/')
            else:
                messages.success(request, 'You can\'t activate exam, no questions exists')
                return redirect('/exam_list/')
        else:
            return redirect('/exam_list/')
    else:
            return redirect('/home/')
    
def active_batch(request):
    if 'master' in request.session:
        if 'b_id' in request.GET:
            obj = Batch.objects.get(b_id=request.GET.get('b_id'))
            obj.status = True
            obj.save()
            messages.success(request, 'Batch is active')
            return redirect('/batch_list/')
        else:
            return redirect('/batch_list/')
    else:
            return redirect('/home/')

def active_assignment(request):
    if 'teacher' in request.session:
        if 'a_id' in request.GET:
            obj = Assignment.objects.get(a_id=request.GET.get('a_id'))
            obj.status = True
            obj.save()
            messages.success(request, 'Assignment is active')
            return redirect('/assignment_list/')
        else:
            return redirect('/assignment_list/')
    else:
            return redirect('/home/')

def questions(request):
    if 'teacher' in request.session:
        if request.method == 'POST':
            obj = Questions()
            obj.exam_id = request.POST['exam_id']
            obj.question = request.POST.get('question')
            obj.optionA = request.POST.get('optionA')
            obj.optionB = request.POST.get('optionB')
            obj.optionC = request.POST.get('optionC')
            obj.optionD = request.POST.get('optionD')
            answer = request.POST.get('answer')
            if answer == 'optionA':
                obj.answer = request.POST.get('optionA')
            elif answer == 'optionB':
                obj.answer = request.POST.get('optionB')
            elif answer == 'optionC':
                obj.answer = request.POST.get('optionC')
            else:
                obj.answer = request.POST.get('optionD')
            obj.save()
            messages.success(request, 'Submitted successfully.')
            return redirect('/questions?e_id='+request.POST.get('exam_id'))
        elif 'e_id' in request.GET:
            data = Exam.objects.get(e_id=request.GET['e_id'])
            return render(request,'teacher/questions.html',{'data':data})
        else:
            return redirect('/exam_list/')
    else:
        return redirect('/home/')
    
def edit_question(request):
    if 'teacher' in request.session:
        if request.method == 'POST':
            obj = Questions.objects.get(q_id=request.POST.get('q_id'))
            obj.question = request.POST.get('question')
            obj.optionA = request.POST.get('optionA')
            obj.optionB = request.POST.get('optionB')
            obj.optionC = request.POST.get('optionC')
            obj.optionD = request.POST.get('optionD')
            answer = request.POST.get('answer')
            if answer == 'optionA':
                obj.answer = request.POST.get('optionA')
            elif answer == 'optionB':
                obj.answer = request.POST.get('optionB')
            elif answer == 'optionC':
                obj.answer = request.POST.get('optionC')
            else:
                obj.answer = request.POST.get('optionD')
            obj.save()
            messages.success(request, 'Updated successfully.')
            return redirect('/exam_list/')
        elif 'q_id' in request.GET:
            data = Questions.objects.get(q_id=request.GET.get('q_id'))
            return render(request,'teacher/edit_question.html',{'data':data})
        else:
            return redirect('/exam_list/')
    else:
        return redirect('/home/')
    
def attend_exam(request):
    if 'student' in request.session:
        if request.method == 'POST':
            question_ids = request.POST.getlist('question_id')

            for q_id in question_ids:
                answer = request.POST.get('answer_'+q_id)
                if answer:  
                    Answers.objects.create(question_id=q_id, answer=answer,student_id=request.session['student'])
                else:
                    Answers.objects.create(question_id=q_id,student_id=request.session['student'])
            return redirect('/my_course/')
        
        elif 'e_id' in request.GET:
            exam = Exam.objects.get(e_id=request.GET['e_id'])
            data = Questions.objects.filter(exam_id=request.GET.get('e_id')).select_related('exam')
            
            countdown = timedelta(minutes=exam.duration)
            m=str(countdown)
            print(m)
            json_data = json.dumps(m)
            return render(request,'student/attend_exam.html',{'data':data,'json_data':json_data,'exam':exam})
        else:
            return redirect('/exam_list/')
    else:
        return redirect('/home/')


def chat(request):
    if 'student' in request.session:
        if request.method == 'POST':
            obj = Doubts()
            obj.receiver_id = request.POST['receiver_id']
            obj.sender_id = request.session['login_id']
            obj.msg = request.POST['msg']
            obj.save()
            return redirect('/video_play?l_id='+request.POST['l_id'])
        else:
            data = Batch.objects.get(b_id=request.GET['b_id'])
            return render(request,'student/join_batch.html',{'data':data})
    elif  'teacher' in request.session:
        if request.method == 'POST':
            obj = Doubts()
            obj.receiver_id = request.POST['receiver_id']
            obj.sender_id = request.session['login_id']
            obj.msg = request.POST['msg']
            obj.save()
            str1 = ''
            student_id = request.POST['receiver_id']
            teacher_id = request.session['login_id']
            data = (
                    Doubts.objects.filter(
                        Q(sender_id=student_id, receiver_id=teacher_id) |
                        Q(sender_id=teacher_id, receiver_id=student_id)
                    )
                    .select_related('sender', 'receiver') 
                    .order_by('msg_date') 
                )
            for i in data:
                formatted_date = i.msg_date.strftime("%B %d, %Y, %I:%M %p").lower()
                if i.sender_id == request.session['login_id']:
                    str1+=f'''<div class="col-12">
                        <div class="mt-2 bg-white border rounded p-2 w-75 float-end" style="font-size: small;">
                            {i.msg}
                            <p class="mb-0 mt-2" style="font-size: xx-small;">{formatted_date}</p>
                        </div>
                    </div>'''
                else:
                    str1+=f'''<div class="col-12">
                        <div class="mt-2 bg-light border rounded p-2 w-75" style="font-size: small;">
                            {i.msg}
                            <p class="mt-2 mb-0" style="font-size: xx-small;">{formatted_date}</p>
                        </div>
                    </div>'''
            return HttpResponse(str1)
        else:
            if 'student_id' in request.GET:
                teacher_id = request.session['login_id']  

                latest_date_subquery = Doubts.objects.filter(
                    Q(sender_id=OuterRef('student_id'), receiver_id=teacher_id) |
                    Q(receiver_id=OuterRef('student_id'), sender_id=teacher_id)
                ).order_by('-msg_date').values('msg_date')[:1]

                data = (
                    Doubts.objects.filter(Q(receiver_id=teacher_id) | Q(sender_id=teacher_id))
                    .annotate(
                        student_id=Case(
                            When(receiver_id=teacher_id, then="sender_id"),
                            When(sender_id=teacher_id, then="receiver_id"),
                            output_field=IntegerField(),
                        )
                    )
                    .values("student_id") 
                    .annotate(
                        student_name=Max(
                            Case(
                                When(receiver_id=teacher_id, then="sender__student_register__name"),
                                When(sender_id=teacher_id, then="receiver__student_register__name"),
                                output_field=CharField(),
                            )
                        ),
                        student_image=Max(
                            Case(
                                When(receiver_id=teacher_id, then="sender__student_register__image"),
                                When(sender_id=teacher_id, then="receiver__student_register__image"),
                                output_field=CharField(),
                            )
                        ),
                        latest_date=Subquery(latest_date_subquery),
                        unread_count=Count(
                            Case(
                                When(receiver_id=teacher_id, status=False, then=1),
                                output_field=IntegerField()
                            )
                        )
                    )
                    .order_by('-latest_date')  
                    )
                
                student_id = request.GET.get('student_id')


                student = Student_register.objects.get(login_id=student_id)

                chatdata = (
                    Doubts.objects.filter(
                        Q(sender_id=student_id, receiver_id=teacher_id) |
                        Q(sender_id=teacher_id, receiver_id=student_id)
                    )
                    .select_related('sender', 'receiver') 
                    .order_by('msg_date') 
                )
                Doubts.objects.filter(
                        Q(sender_id=student_id, receiver_id=teacher_id),status=False
                    ).update(status=True)
            return render(request,'teacher/chat.html',{'data':data,'chatdata':chatdata,'student':student})
    else:
        return redirect('/home/')

def doubt(request):
    if 'teacher' in request.session:
        teacher_id = request.session['login_id']  

        latest_date_subquery = Doubts.objects.filter(
            Q(sender_id=OuterRef('student_id'), receiver_id=teacher_id) |
            Q(receiver_id=OuterRef('student_id'), sender_id=teacher_id)
        ).order_by('-msg_date').values('msg_date')[:1]

        data = (
            Doubts.objects.filter(Q(receiver_id=teacher_id) | Q(sender_id=teacher_id))
            .annotate(
                student_id=Case(
                    When(receiver_id=teacher_id, then="sender_id"),
                    When(sender_id=teacher_id, then="receiver_id"),
                    output_field=IntegerField(),
                )
            )
            .values("student_id") 
            .annotate(
                student_name=Max(
                    Case(
                        When(receiver_id=teacher_id, then="sender__student_register__name"),
                        When(sender_id=teacher_id, then="receiver__student_register__name"),
                        output_field=CharField(),
                    )
                ),
                student_image=Max(
                    Case(
                        When(receiver_id=teacher_id, then="sender__student_register__image"),
                        When(sender_id=teacher_id, then="receiver__student_register__image"),
                        output_field=CharField(),
                    )
                ),
                latest_date=Subquery(latest_date_subquery),
                unread_count=Count(
                    Case(
                        When(receiver_id=teacher_id, status=False, then=1),
                        output_field=IntegerField()
                    )
                )
            )
            .order_by('-latest_date')  
            )
        return render(request,'teacher/chat.html',{'data':data})
    elif 'student' in request.session:
        if request.method == 'POST':
            obj = Doubts()
            obj.receiver_id = request.POST['receiver_id']
            obj.sender_id = request.session['login_id']
            obj.msg = request.POST['msg']
            obj.save()
            str1 = ''
            teacher_id = request.POST['receiver_id']
            student_id = request.session['login_id'] 
            data = (
                        Doubts.objects.filter(
                            Q(sender_id=student_id, receiver_id=teacher_id) |
                            Q(sender_id=teacher_id, receiver_id=student_id)
                        )
                        .select_related('sender', 'receiver') 
                        .order_by('msg_date') 
                    )
            for i in data:
                formatted_date = i.msg_date.strftime("%B %d, %Y, %I:%M %p").lower()
                if i.sender_id == request.session['login_id']:
                    str1+=f'''<div class="col-12">
                        <div class="mt-2 bg-white border p-2 w-75 float-end" style="font-size: small;border-radius: 5px;">
                            {i.msg}
                            <p class="mb-0 mt-2" style="font-size: xx-small;">{formatted_date}</p>
                        </div>
                        
                    </div>'''
                else:
                    str1+=f'''<div class="col-12">
                        <div class="mt-2 bg-light border p-2 w-75" style="font-size: small;border-radius: 5px;">
                            {i.msg}
                            <p class="mt-2 mb-0" style="font-size: xx-small;">{formatted_date}</p>
                        </div>
                    </div>'''
            return HttpResponse(str1)
        elif 'teacher_id' in request.GET:
            student_id = request.session['login_id'] 

            batch = Batch.objects.get(b_id=request.GET.get('b_id'))
            ids = list(batch.teacher.values_list('login_id', flat=True))
            
            latest_date_subquery = Doubts.objects.filter(
                Q(sender_id=OuterRef('teacher_id'), receiver_id=student_id) |
                Q(receiver_id=OuterRef('teacher_id'), sender_id=student_id)
            ).order_by('-msg_date').values('msg_date')[:1]


            data = (
                Doubts.objects.filter(Q(receiver_id__in=ids) | Q(sender_id__in=ids)).filter(Q(receiver_id=student_id) | Q(sender_id=student_id))
                .annotate(
                    teacher_id=Case(
                        When(receiver_id=student_id, then="sender_id"),
                        When(sender_id=student_id, then="receiver_id"),
                        output_field=IntegerField(),
                    )
                )
                .values("teacher_id") 
                .annotate(
                    teacher_name=Max(
                        Case(
                            When(receiver_id=student_id, then="sender__teacher_register__name"),
                            When(sender_id=student_id, then="receiver__teacher_register__name"),
                            output_field=CharField(),
                        )
                    ),
                    teacher_image=Max(
                        Case(
                            When(receiver_id=student_id, then="sender__teacher_register__image"),
                            When(sender_id=student_id, then="receiver__teacher_register__image"),
                            output_field=CharField(),
                        )
                    ),
                    latest_date=Subquery(latest_date_subquery),
                    unread_count=Count(
                        Case(
                            When(receiver_id=student_id, status=False, then=1),
                            output_field=IntegerField()
                        )
                    )
                )
                .order_by('-latest_date')  
                )
                
            teacher_id = request.GET.get('teacher_id')
            

            teacher = Teacher_register.objects.get(login_id=teacher_id)

            chatdata = (
                Doubts.objects.filter(
                    Q(sender_id=student_id, receiver_id=teacher_id) |
                    Q(sender_id=teacher_id, receiver_id=student_id)
                )
                .select_related('sender', 'receiver') 
                .order_by('msg_date') 
            )
            Doubts.objects.filter(
                        Q(sender_id=teacher_id, receiver_id=student_id),status=False
                    ).update(status=True)
            return render(request,'student/chat.html',{'data':data,'chatdata':chatdata,'teacher':teacher,'b_id':batch.b_id})
        else:
            if 'b_id' in request.GET:
                student_id = request.session['login_id']  

                batch = Batch.objects.get(b_id=request.GET.get('b_id'))
                ids = list(batch.teacher.values_list('login_id', flat=True))

                latest_date_subquery = Doubts.objects.filter(
                    Q(sender_id=OuterRef('teacher_id'), receiver_id=student_id) |
                    Q(receiver_id=OuterRef('teacher_id'), sender_id=student_id)
                ).order_by('-msg_date').values('msg_date')[:1]

                data = (
                    Doubts.objects.filter(Q(receiver_id__in=ids) | Q(sender_id__in=ids)).filter(Q(receiver_id=student_id) | Q(sender_id=student_id))
                    .annotate(
                        teacher_id=Case(
                            When(receiver_id=student_id, then="sender_id"),
                            When(sender_id=student_id, then="receiver_id"),
                            output_field=IntegerField(),
                        )
                    )
                    .values("teacher_id") 
                    .annotate(
                        teacher_name=Max(
                            Case(
                                When(receiver_id=student_id, then="sender__teacher_register__name"),
                                When(sender_id=student_id, then="receiver__teacher_register__name"),
                                output_field=CharField(),
                            )
                        ),
                        teacher_image=Max(
                            Case(
                                When(receiver_id=student_id, then="sender__teacher_register__image"),
                                When(sender_id=student_id, then="receiver__teacher_register__image"),
                                output_field=CharField(),
                            )
                        ),
                        latest_date=Subquery(latest_date_subquery),
                        unread_count=Count(
                            Case(
                                When(receiver_id=student_id, status=False, then=1),
                                output_field=IntegerField()
                            )
                        )
                    )
                    .order_by('-latest_date')  
                    )
                return render(request,'student/chat.html',{'data':data,'b_id':batch.b_id})
            else:
                return redirect('/my_course/')
    else:
        return redirect('/home/')
    
def progress(request):
    if 'b_id' in request.GET:
        batch = Batch.objects.get(b_id=request.GET.get('b_id'))
        if 'student' in request.session:
            std = Student_register.objects.get(sr_id=request.session['student'])
            data = (
                Exam.objects
                .filter(questions__answers__student_id=request.session['student'],batch=request.GET.get('b_id'))
                .annotate(
                    total_marks=Sum(
                        Case(
                            When(
                                questions__answers__answer=F('questions__answer'),
                                then=1 
                            ),
                            default=0,
                            output_field=IntegerField()
                        )
                    ),
                    total_questions=Count('questions')
                )
                .select_related('teacher')  
            )

            data2 = (
                Assignment.objects.filter(
                    batch__b_id=request.GET.get('b_id'),
                    submission__student_id=request.session['student'],
                    submission__mark__isnull=False  
                )
                .annotate(
                    tmark=F('total_mark'),
                    smark=F('submission__mark')
                )
                .prefetch_related('batch')
                .select_related('teacher')
            )
           
            totals_ex = None
            totals_ass = None
            if data:
                totals_ex = data.aggregate(tm=Sum('total_marks'),tq=Sum('total_questions')) or {'tm': 0, 'tq': 0}
            if data2:
                totals_ass = data2.aggregate(tm=Sum('tmark'),sm=Sum('smark')) or {'tm': 0, 'sm': 0}
            
            if totals_ex and totals_ass:
                t = totals_ex['tq']+totals_ass['tm']
                s = totals_ex['tm']+totals_ass['sm']
                pro = round((s/t)*100)
                json_data = json.dumps(pro)
            elif totals_ex:
                pro = round((totals_ex['tm']/totals_ex['tq'])*100)
                json_data = json.dumps(pro)
            elif totals_ass:
                pro = round((totals_ass['sm']/totals_ass['tm'])*100)
                json_data = json.dumps(pro)
            else:
                json_data = 0

            return render(request,'student/progress.html',{'data':data,'pro':json_data,'data2':data2,'totals_ex':totals_ex,'totals_ass':totals_ass,'batch':batch,'std':std})
    else:
        return redirect('/home/')
    
def progress_report(request):
    if 'b_id' and 'sr_id' in request.GET:
        batch = Batch.objects.get(b_id=request.GET.get('b_id'))
        std = Student_register.objects.get(sr_id=request.GET.get('sr_id'))
        data = (
            Exam.objects
            .filter(questions__answers__student_id=request.GET.get('sr_id'),batch=request.GET.get('b_id'))
            .annotate(
                total_marks=Sum(
                    Case(
                        When(
                            questions__answers__answer=F('questions__answer'),
                            then=1 
                        ),
                        default=0,
                        output_field=IntegerField()
                    )
                ),
                total_questions=Count('questions')
            )
            .select_related('teacher')  
        )

        data2 = (
            Assignment.objects.filter(
                batch__b_id=request.GET.get('b_id'),
                submission__student_id=request.GET.get('sr_id'),
                submission__mark__isnull=False  
            )
            .annotate(
                tmark=F('total_mark'),
                smark=F('submission__mark')
            )
            .prefetch_related('batch')
            .select_related('teacher')
        )

        totals_ex = None
        totals_ass = None
        if data:
            totals_ex = data.aggregate(tm=Sum('total_marks'),tq=Sum('total_questions')) or {'tm': 0, 'tq': 0}
        if data2:
            totals_ass = data2.aggregate(tm=Sum('tmark'),sm=Sum('smark')) or {'tm': 0, 'sm': 0}

        if totals_ex and totals_ass:
            t = totals_ex['tq']+totals_ass['tm']
            s = totals_ex['tm']+totals_ass['sm']
            pro = round((s/t)*100)
            json_data = json.dumps(pro)
        elif totals_ex:
            pro = round((totals_ex['tm']/totals_ex['tq'])*100)
            json_data = json.dumps(pro)
        elif totals_ass:
            pro = round((totals_ass['sm']/totals_ass['tm'])*100)
            json_data = json.dumps(pro)
        else:
            json_data = 0

        if 'teacher' in request.session:
            return render(request,'teacher/progress.html',{'data':data,'pro':json_data,'data2':data2,'totals_ex':totals_ex,'totals_ass':totals_ass,'batch':batch,'std':std})
        elif 'master' in request.session:
            return render(request,'master/progress.html',{'data':data,'pro':json_data,'data2':data2,'totals_ex':totals_ex,'totals_ass':totals_ass,'batch':batch,'std':std})
        else:
            return redirect('/home/')
    else:
            return redirect('/home/')   
    
def batch_students(request):
    if 'b_id' in request.GET:
        batch = Batch.objects.get(b_id=request.GET.get('b_id'))
        data = Student_register.objects.filter(enrollment__batch_id=request.GET.get('b_id')).select_related('login')
        if 'teacher' in request.session:
            return render(request,'teacher/batch_students.html',{'data':data,'batch':batch})
        elif 'master' in request.session:
            return render(request,'master/batch_students.html',{'data':data,'batch':batch})
    return redirect('/home/')

def feedback(request):
    if 'student' in request.session:
        if request.method == 'POST':
            obj = Feedback()
            obj.feedback = request.POST['feedback']
            obj.student_id = request.session['student']
            obj.save()
            messages.success(request, 'Submitted successfully.')
            return redirect('/feedback/')
        else:
            data = Feedback.objects.select_related('student')
            return render(request,'student/feedback.html',{'data':data})
    elif 'master' in request.session:
        data = Feedback.objects.select_related('student').order_by('-f_id')
        return render(request,'master/feedback.html',{'data':data})
    else:
        return redirect('/home/')
    
def receipt(request):
    data = Enrollment.objects.get(e_id=request.GET.get('e_id'))
    id = request.GET['e_id']
    response = HttpResponse (content_type="application/pdf")
    response['Content-Disposition'] = f'attachment; filename="reciept_{id}.pdf"'

    domain = "http://localhost:8000"
    logo_url = domain + static('user/img/download.png')

    html = render_to_string('student/receipt_pdf.html', {'data': data,'logo_url': logo_url})

    pisa_status = pisa.CreatePDF(html, dest=response) 

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')   
    return response

def profile(request):
    if 'teacher' in request.session:
        if request.method == 'POST':
            obj = Teacher_register.objects.get(tr_id=request.session['teacher'])
            obj.name = request.POST['name']
            obj.email = request.POST['email']
            obj.contact_number = request.POST['contact_number']
            obj.address = request.POST['address']
            if 'image' in request.FILES:
                im=request.FILES['image']
                ob = FileSystemStorage()
                fl = ob.save(im.name,im)
                
                obj.image = ob.url(fl)
            obj.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('/profile/')
        else:
            data = Teacher_register.objects.get(tr_id=request.session['teacher'])
            return render(request,'teacher/profile.html',{'data':data})
    elif 'student' in request.session:
        if request.method == 'POST':
            obj = Student_register.objects.get(sr_id=request.session['student'])
            obj.name = request.POST['name']
            obj.email = request.POST['email']
            obj.contact_number = request.POST['contact_number']
            obj.address = request.POST['address']
            if 'image' in request.FILES:
                im=request.FILES['image']
                ob = FileSystemStorage()
                fl = ob.save(im.name,im)
                
                obj.image = ob.url(fl)
            obj.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('/profile/')
        else:
            data = Student_register.objects.get(sr_id=request.session['student'])
            return render(request,'student/profile.html',{'data':data})
    else:
        return redirect('/home/')

def change_password(request):
    if request.method == 'POST':
        try:
            obj = Login.objects.get(login_id=request.session['login_id'])
            if obj.password == request.POST['current_password']:
                obj.password=request.POST['password']
                obj.save()
                messages.success(request, 'Your password has been reset successfully.')
                return redirect('/change_password/')
            else:
                messages.success(request, 'Enter valid current password',extra_tags='msg')
                return redirect('/change_password/')
        except Exception:
            messages.success(request, 'Invalid User',extra_tags='msg')
            return redirect('/change_password/')
    else:
        if 'teacher' in request.session:
            return render(request,'teacher/change_password.html')
        elif 'student' in request.session:
            return render(request,'student/change_password.html')
        else:
            return redirect('/home')  
        
def search_course(request):
    if 'master' in request.session:
        str1 = ''
        data = Course.objects.filter(course_name__icontains=request.GET.get('cname')).select_related('category')
        if data:
            c = 0
            for i in data:
                c += 1
                short_desc = Truncator(i.description).chars(60, truncate='...')
                full_desc = i.description.replace("\n", "<br>")  
                
                subjects_list = ", ".join([subject.subject for subject in i.subjects.all()])

                str1 +=f'''<tr>
                    <th>{c}</th>
                    <td>
                        {i.course_name} <br>'''
                        
                if i.certificate_course:
                    str1+='<small class="text-danger">Certificate course</small>'
                        
                            
                str1+='</td><td>'
                if i.image:
                    str1+=f'''<img src="{i.image}" height="55" width="80" class="rounded" alt="">'''
                else:
                    str1+='<img src="../../static/user/img/ol.jpg" height="55" width="80" class="rounded" alt="">'
                        
                str1+=f'''</td>
                    <td>
                        <div class="article-container">
                            <p id="short-text-{ i.c_id }" class="short-text">{ short_desc }...</p>
                            
                            <p id="full-text-{ i.c_id }" class="full-text" style="display:none;">{ full_desc }</p>
                            
                            <a href="javascript:void(0);" id="read-more-{ i.c_id }" onclick="toggleText('{ i.c_id }')" class="read-more small">Read More</a>
                        </div>
                    </td>
                    <td>{subjects_list}</td>
                    <td>{i.fees}</td>

                    <td><a href="/edit_course/?c_id={i.c_id}" class="btn btn-sm btn-primary">Edit</a></td>
                    <td><a href="/delete_course/?c_id={i.c_id}" class="btn btn-sm btn-danger">Delete</a></td>
                </tr>'''
        else:
            str1+= '<tr><td colspan="7"><b class="font-monospace text-danger">Not found any Course</b></td></tr>'
        return HttpResponse(str1)

    str1 = ''
    category=request.GET['category'].split(",")
    fees=request.GET['fees'].split(",")
    mon=request.GET['mon'].split(",")

    if len(fees)==1 and '40000+' in fees:
        fees_query = Q(fees__gte=40000)
    elif len(fees) > 1 and '40000+' in fees:
        fees_query = Q(fees__gte=int(fees[0]))
    elif fees != ['']:
        fees_query = Q(fees__gte=int(fees[0]),fees__lte=int(fees[-1]))
    else:
        fees_query = Q()

    if category != ['']:
        category_query=Q(category_id__in=category)
    else:
        category_query=Q()
   
    if mon != ['']:
        if len(mon)==1 and '-1' in mon:
            mont = Q(duration_months__lte=1)
        elif len(mon)>1 and '-1' in mon:
            mont = Q(duration_months__gte=int(mon[0]),duration_months__lte=int(mon[-1]))
        elif len(mon)==1 and '12+' in mon:
            mont = Q(duration_months__gte=12)
        elif len(mon) > 1 and '12+' in mon:
            mont = Q(duration_months__gte=int(mon[0]))
        elif len(mon) > 1:
            mont = Q(duration_months__gte=int(mon[0]),duration_months__lte=int(mon[-1]))
        else:
            mont = Q()
            
        batches = Batch.objects.annotate(
            start_year=ExtractYear('start_date'),
            start_month=ExtractMonth('start_date'),
            end_year=ExtractYear('end_date'),
            end_month=ExtractMonth('end_date'),
            duration_months=((F('end_year') - F('start_year')) * 12) + (F('end_month') - F('start_month'))
        ).filter(mont)
        
        data = Course.objects.filter(category_query,fees_query,batch__in=batches).distinct()
    else:
        data = Course.objects.filter(category_query,fees_query).select_related('category')

    if data:
        for i in data:
            str1+=f'''
                <div class="col-lg-6">
                                <a href="/batches/?course_id={ i.c_id }" class="shadow-lg">
                                    <div class="d-flex align-items-center p-3 bg-white rounded">'''
            if i.image:
                str1+=f'''<img src="{i.image}" class="img-fluid" style="max-width: 7rem;max-height:7rem;border-radius: 1px;" alt="">'''
            else:
                str1+=f'''<img src="../../static/user/img/ol.jpg" class="img-fluid" style="max-width: 7rem;max-height:7rem;border-radius: 1px;" alt="">'''
                                        
            str1+=f'''<div class="ms-3">
                            <p class="h6 mb-2">{ i.course_name }</p>
                            <p class="text-dark mt-3 mb-0 me-3"><span class="btn btn-light btn-sm" style="border-radius: 8px;background-color: rgb(245, 243, 243);">₹ { i.fees }</span></p>
                        </div>
                    </div>
                </a>
            </div>'''
    else:
        str1+= '<h4 class="text-danger text-center">Not Found Course</h4>'
    return HttpResponse(str1)

def search_course_text(request):
    str1 = ''
    data = Course.objects.filter(course_name__icontains=request.GET.get('cname')).select_related('category')
    if data:
        for i in data:
            str1+=f'''
                <div class="col-lg-6">
                                <a href="/batches/?course_id={ i.c_id }" class="shadow-lg">
                                    <div class="d-flex align-items-center p-3 bg-white rounded">'''
            if i.image:
                str1+=f'''<img src="{i.image}" class="img-fluid" style="max-width: 7rem;max-height:7rem;border-radius: 1px;" alt="">'''
            else:
                str1+=f'''<img src="../../static/user/img/ol.jpg" class="img-fluid" style="max-width: 7rem;max-height:7rem;border-radius: 1px;" alt="">'''
                                        
            str1+=f'''<div class="ms-3">
                            <p class="h6 mb-2">{ i.course_name }</p>
                            <p class="text-dark mt-3 mb-0 me-3"><span class="btn btn-light btn-sm" style="border-radius: 8px;background-color: rgb(245, 243, 243);">₹ { i.fees }</span></p>
                        </div>
                    </div>
                </a>
            </div>'''
    else:
        str1+= '<h4 class="text-danger text-center">Not Found Course</h4>'
    return HttpResponse(str1)


def search_teacher(request):
    str1 = ''
    if 'subject' in request.GET:
        check_query = Q(subject_id=request.GET.get('subject'))
    elif 'tname' in request.GET:
        check_query = Q(name__icontains=request.GET.get('tname'))
    data = Teacher_register.objects.filter(check_query).select_related('login','subject')
    if data:
        c = 0
        for i in data:
            c += 1
            str1 +=f'''<tr>
                <th>{c}</th>
                <td>'''
            if i.image:
                str1+=f'''<img src="{ i.image }" height="60" width="60" class="rounded" alt="">'''
            else:
                str1+=f'''<img src="../../static/user/img/dum.jpg" height="60" width="60" class="rounded" alt="">'''
                
            str1+=f'''</td>
            <td>{ i.name }</td>
            <td>
                { i.email } <br>
                { i.contact_number }
            </td>
            <td>{ i.qualification }</td>
            <td>{ i.experience }</td>
            <td>{ i.address }</td>
            <td>{ i.subject.subject }</td>
            </tr>'''
    else:
        str1+= '<tr><td colspan="7"><b class="font-monospace text-danger">Not found any Staff</b></td></tr>'
    return HttpResponse(str1)

def search_student(request):
    str1 = ''
    if 'batch_id' in request.GET:
        check_query = Q(enrollment__batch_id=request.GET.get('batch_id'))
    elif 'sname' in request.GET:
        check_query = Q(name__icontains=request.GET.get('sname'))
    data = Student_register.objects.filter(check_query).select_related('login')
    if data:
        c = 0
        for i in data:
            c += 1
            str1 +=f'''<tr>
                <th>{c}</th>
                <td>'''
            if i.image:
                str1+=f'''<img src="{ i.image }" height="60" width="60" class="rounded" alt="">'''
            else:
                str1+=f'''<img src="../../static/user/img/dum.jpg" height="60" width="60" class="rounded" alt="">'''
                
            str1+=f'''</td>
            <td>{ i.name }</td>
            <td>
                { i.email } <br>
                { i.contact_number }
            </td>
            <td>{ i.address }</td>
            <td>'''
            if i.login.status == False:
                str+=f'''<a href="/login_status?login_id={ i.login_id }&status=True" class="btn btn-sm btn-success">Allow access</a>'''
            else:
                str1+=f'''<a href="/login_status?login_id={ i.login_id }&status=False" class="btn btn-sm btn-danger">Denial access</a>'''
            
            str1+='</td></tr>'
    else:
        str1+= '<tr><td colspan="7"><b class="font-monospace text-danger">Not found any student</b></td></tr>'
    return HttpResponse(str1)

def search_lesson(request):
    str1 = ''
    data = Teacher_register.objects.filter(name__icontains=request.GET.get('tname')).annotate(nov = Count('lessons__l_id')).select_related('login','subject')
    if data:
        c = 0
        for i in data:
            c += 1
            str1 +=f'''<tr>
                <th>{c}</th>
                <td>'''
            if i.image:
                str1+=f'''<img src="{ i.image }" height="60" width="60" class="rounded" alt="">'''
            else:
                str1+=f'''<img src="../../static/user/img/dum.jpg" height="60" width="60" class="rounded" alt="">'''
                
            str1+=f'''</td>
            <td>{ i.name }</td>
            <td>
                { i.email } <br>
                { i.contact_number }
            </td>
            <td>{ i.address }</td>
            <td>{ i.subject.subject }</td>
            <td><a href="/video_list?teacher_id={ i.tr_id }" class="btn btn-sm btn-dark rounded-pill w-75">{ i.nov } videos <i class="bi bi-arrow-right text-primary"></i></a></td>
            </tr>'''
    else:
        str1+= '<tr><td colspan="7"><b class="font-monospace text-danger">Not found any Staff</b></td></tr>'
    return HttpResponse(str1)

def search_batch(request):
    str1 = ''
    if request.GET.get('s') == 'h':
        check_query = Q(end_date__lt=date.today())
    elif request.GET.get('s') == 'a':
        check_query = Q(end_date__gte=date.today())
    else:
        check_query = Q()

    data = Batch.objects.filter(check_query,title__icontains=request.GET.get('bname'),status=True).select_related('course').order_by('b_id')


    if data:
        c = 0
        for i in data:
            teacher_list = ", ".join([teacher.name for teacher in i.teacher.all()])

            c += 1
            str1 +=f'''<tr>
                <th>{c}</th>
                <td>{i.title}</td>
                <td>{i.course.course_name}</td>
                <td>{teacher_list}</td>
                <td>{i.closing_date}</td>
                <td>{i.start_date} - {i.end_date}</td>

                <td><a href="/batch_students?b_id={i.b_id}" class="btn btn-sm btn-dark text-danger">Students </a></a></td></tr>'''
    else:
        str1+= '<tr><td colspan="7"><b class="font-monospace text-danger">Not found any batches</b></td></tr>'
    return HttpResponse(str1)

def search_assignment(request):
    str1 = ''
    data = Assignment.objects.filter(title__icontains=request.GET.get('aname'),teacher_id=request.session['teacher']).select_related('teacher').order_by('-a_id')
    if data:
        c = 0
        for i in data:
            batch_list = ", ".join([batch.title for batch in i.batch.all()])
            short_desc = Truncator(i.description).chars(20, truncate='...')
            full_desc = i.description.replace("\n", "<br>")
            formatted_date = i.created_at.strftime("%B %d, %Y, %I:%M %p").lower()
            c += 1
            str1 +=f'''<tr>
                <th>{c}</th>
                <td>{ i.title }</td>   
            <td>
                <div class="article-container">
                    <p id="short-text-{ i.a_id }" class="short-text">{ short_desc }...</p>
                    
                    <p id="full-text-{ i.a_id }" class="full-text" style="display:none;">{ full_desc }</p>
                    
                    <a href="javascript:void(0);" id="read-more-{ i.a_id }" onclick="toggleText('{ i.a_id }')" class="read-more small">Read More</a>
                </div>
            </td>
            <td>{ batch_list }</td>  
            <td>{i.due_date} </td>
            <td>{i.total_mark}</td>
            <td>{formatted_date}</td>
            <td>'''
                
            if i.status == False:
                str1+=f'''<a href="/edit_assignment?a_id={i.a_id}" class="btn btn-sm btn-primary">Edit</a>
                <button type="button" class="btn btn-sm btn-warning my-1" data-bs-toggle="modal" data-bs-target="#verticalycentered{ c }">
                    Publish
                </button>
                <div class="modal fade" id="verticalycentered{ c }" tabindex="-1" aria-hidden="true" style="display: none;">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">Publish assignment</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="alert alert-danger px-1 alert-dismissible fade show" role="alert">
                                    <h6 class="fw-bold">Are you sure you want to set assignment as active?</h6>
                                    <hr>
                                    <p class="text-warning h6"><i class="bi bi-exclamation-triangle"></i> Alert</p>
                                    <p class="mb-0">Once the assignment is activated, you will not be able to edit.</p>
                                </div>
                                <div class="d-flex justify-content-end">
                                    <button type="button" class="btn btn-sm btn-danger px-4" data-bs-dismiss="modal">No</button>
                                    <a href="/active_assignment/?a_id={ i.a_id }" class="btn btn-sm btn-primary px-4 ms-2">Yes</a>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                </div>'''
            else:
                str1+='<div class="badge badge-primary bg-primary">Active</div>'
                   
            str1+=f'''</td>
            <td><a href="/delete_assignment?a_id={i.a_id}" class="btn btn-sm btn-danger">Delete</a></td>
            </tr>'''
    else:
        str1+= '<tr><td colspan="7"><b class="font-monospace text-danger">Not found any Staff</b></td></tr>'
    return HttpResponse(str1)

def search_submission(request):
    str1 = ''
    data = Assignment.objects.filter(title__icontains=request.GET.get('aname'),teacher_id=request.session['teacher']).select_related('teacher').order_by('-a_id')
    if data:
        c = 0
        for i in data:
            formatted_date = i.created_at.strftime("%B %d, %Y, %I:%M %p").lower()
            short_desc = Truncator(i.description).chars(20, truncate='...')
            full_desc = i.description.replace("\n", "<br>")
            c += 1
            str1 +=f'''<tr>
                <th>{c}</th>
                <td>{ i.title }</td>   
            <td>
                <div class="article-container">
                    <p id="short-text-{ i.a_id }" class="short-text">{ short_desc }...</p>
                    
                    <p id="full-text-{ i.a_id }" class="full-text" style="display:none;">{ full_desc }</p>
                    
                    <a href="javascript:void(0);" id="read-more-{ i.a_id }" onclick="toggleText('{ i.a_id }')" class="read-more small">Read More</a>
                </div>
            </td>
            
            <td>{i.due_date} </td>
            <td>{i.total_mark}</td>
            <td>{formatted_date}</td>
            <td>'''
            for j in i.batch.all():
                str1+=f'''<a href="/batch_assignment?b_id={ j.b_id }&a_id={ i.a_id }" class="text-success">{ j.title } <i class="bi bi-arrow-right"></i></a><br>'''
                                        
            str1+='</tr>'
    else:
        str1+= '<tr><td colspan="7"><b class="font-monospace text-danger">Not found any Staff</b></td></tr>'
    return HttpResponse(str1)

def search_exam(request):
    str1 = ''

    data = Exam.objects.filter(teacher=request.session['teacher'],title__icontains=request.GET.get('ename')).annotate(
                    et = Case(
                        When(Q(duration__gt=59),
                             then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                             default=Concat(F('duration'), Value('m')),
                             output_field=CharField()
                    )
                ).select_related('teacher').order_by('-e_id')
    if data:
        c = 0
        for i in data:
            batch_title = i.batch.all().first().title if i.batch.exists() else "N/A"

            short_desc = Truncator(i.topic).chars(50, truncate='...')
            
            c += 1
            str1 +=f'''<tr>
                <th>{c}</th>
                <td>{ i.title }</td>   
            <td>{ short_desc } </td>
            <td>{ i.et }</td>
            <td>{ batch_title }...</td>
            <td>'''
                
            if i.status == False:
                str1+=f'''<button type="button" class="btn btn-sm btn-warning mb-1" data-bs-toggle="modal" data-bs-target="#verticalycentered{ c }">
                    Publish
                </button>
                <div class="modal fade" id="verticalycentered{ c }" tabindex="-1" aria-hidden="true" style="display: none;">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">Publish exam</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="alert alert-danger px-1 alert-dismissible fade show" role="alert">
                                    <h6 class="fw-bold">Are you sure you want to set exam as active?</h6>
                                    <hr>
                                    <p class="text-warning h6"><i class="bi bi-exclamation-triangle"></i> Alert</p>
                                    <p class="mb-0">Once the exam is activated, you will not be able to add questions.</p>
                                </div>
                                <div class="d-flex justify-content-end">
                                    <button type="button" class="btn btn-sm btn-danger px-4" data-bs-dismiss="modal">No</button>
                                    <a href="/active_exam?e_id={ i.e_id }" class="btn btn-sm btn-primary px-4 ms-2">Yes</a>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                </div>'''
            else:
                str1+='<div class="badge badge-primary bg-primary">Active</div>'

            str1+=f'''</td>
            <td>
                <a href="/exam_details?e_id={i.e_id}" class="btn btn-sm btn-dark">Details</a>
            
            </td><td>'''
            if i.status == False:
                    str1+=f'''<a href="/questions?e_id={i.e_id}" class="btn btn-sm btn-success">Questions</a>'''
                
                                  
            str1+='</td></tr>'
    else:
        str1+= '<tr><td colspan="7"><b class="font-monospace text-danger">Not found any Exam</b></td></tr>'
    return HttpResponse(str1)

def search_result(request):
    str1 = ''

    data = Exam.objects.filter(teacher_id=request.session['teacher'],title__icontains=request.GET.get('ename')).annotate(
                    et = Case(
                        When(Q(duration__gt=59),
                             then=Concat(Cast(F('duration') / 60, FloatField()), Value('h'))),
                             default=Concat(F('duration'), Value('m')),
                             output_field=CharField()
                    )
                ).select_related('teacher').order_by('-e_id')
    
    if data:
        c = 0
        for i in data:
            
            c += 1
            str1 +=f'''<tr>
                <th>{c}</th>
                <td>{ i.title }</td>   
            <td>{ i.et }</td>
            <td>'''
            for j in i.batch.all():
                str1+=f'''<a href="/exam_results?e_id={i.e_id}&b_id={ j.b_id }" class="text-success d-block">{ j.title } <i class="bi bi-arrow-right"></i></a>'''
                  
            str1+=f'''</td>
            
            <td>
                <a href="/exam_details?e_id={i.e_id}" class="btn btn-sm btn-dark">Details</a>
                
            </td>            
            </tr>'''
    else:
        str1+= '<tr><td colspan="7"><b class="font-monospace text-danger">Not found any Exam</b></td></tr>'
    return HttpResponse(str1)

def search_enrollment(request):
    str1 = ''
    batch_id = request.GET.get('batch_id')
    data = Enrollment.objects.filter(batch_id=batch_id).select_related('batch','student').order_by('e_id')
    if data:
        c = 0
        for i in data:
            formatted_date = i.enrolled_at.strftime("%B %d, %Y, %I:%M %p").lower()
            c += 1
            str1 +=f'''<tr>
                <th>{ c }</th>
                <td>{ i.batch.title}</td>
                <td>{ i.batch.course.course_name}</td>
                <td>'''
                    
            if i.student.image:
                str1+=f'''<img src="{ i.student.image}" height="60" width="60" class="rounded" alt="">'''
            else:
                str1+='<img src="../static/user/img/dum.jpg" height="60" width="60" class="rounded" alt="">'
                    
            str1+=f'''</td>       
                <th>{ i.student.name}</th>
                <td>{ i.student.email} <br>
                    { i.student.contact_number}
                </td>
                <td>{ formatted_date }</td>

                <td>{  i.amount }</td>
            </tr>'''
    else:
        str1+= '<tr><td colspan="7"><b class="font-monospace text-danger">Not found any Enrollment</b></td></tr>'
    return HttpResponse(str1)

def chat_teacher(request):
    str1 = ''
    student_id = request.GET.get('student_id')
    teacher_id = request.session['login_id']
    data = (
            Doubts.objects.filter(
                Q(sender_id=student_id, receiver_id=teacher_id) |
                Q(sender_id=teacher_id, receiver_id=student_id)
            )
            .select_related('sender', 'receiver') 
            .order_by('msg_date') 
        )
    for i in data:
        formatted_date = i.msg_date.strftime("%B %d, %Y, %I:%M %p").lower()
        if i.sender_id == request.session['login_id']:
            str1+=f'''<div class="col-12">
                <div class="mt-2 bg-white border rounded p-2 w-75 float-end" style="font-size: small;">
                    {i.msg}
                    <p class="mb-0 mt-2" style="font-size: xx-small;">{formatted_date}</p>
                </div>
            </div>'''
        else:
            str1+=f'''<div class="col-12">
                <div class="mt-2 bg-light border rounded p-2 w-75" style="font-size: small;">
                    {i.msg}
                    <p class="mt-2 mb-0" style="font-size: xx-small;">{formatted_date}</p>
                </div>
            </div>'''
    Doubts.objects.filter(
                        Q(sender_id=student_id, receiver_id=teacher_id),status=False
                    ).update(status=True)
    return HttpResponse(str1)

def chat_user(request):
    str1 = ''
    teacher_id = request.GET.get('teacher_id')
    student_id = request.session['login_id'] 
    data = (
                Doubts.objects.filter(
                    Q(sender_id=student_id, receiver_id=teacher_id) |
                    Q(sender_id=teacher_id, receiver_id=student_id)
                )
                .select_related('sender', 'receiver') 
                .order_by('msg_date') 
            )
    
    for i in data:
        formatted_date = i.msg_date.strftime("%B %d, %Y, %I:%M %p").lower()
        if i.sender_id == request.session['login_id']:
            str1+=f'''<div class="col-12">
                <div class="mt-2 bg-white border p-2 w-75 float-end" style="font-size: small;border-radius: 5px;">
                    {i.msg}
                    <p class="mb-0 mt-2" style="font-size: xx-small;">{formatted_date}</p>
                </div>
                
            </div>'''
        else:
            str1+=f'''<div class="col-12">
                <div class="mt-2 bg-light border p-2 w-75" style="font-size: small;border-radius: 5px;">
                    {i.msg}
                    <p class="mt-2 mb-0" style="font-size: xx-small;">{formatted_date}</p>
                </div>
            </div>'''
    Doubts.objects.filter(
                        Q(sender_id=teacher_id, receiver_id=student_id),status=False
                    ).update(status=True)
    return HttpResponse(str1)   

def ed_teacher(request):
    try:
        dis = Teacher_register.objects.filter(subject__course__c_id=request.GET.get("course_id")).select_related('login','subject')
        tr = Batch.objects.get(b_id=request.GET.get("batch_id"))

        ids = tr.teacher.all().values_list('tr_id', flat=True)
        teacher_details = list(dis.values('tr_id', 'name', 'subject__subject'))
        
    except Exception:
        data = {'error_message': 'error'}
        return JsonResponse(data)
    data = {
        'teacher_details': teacher_details,  
        'teacher_ids': list(ids) 
    }
    
    return JsonResponse(data, safe=False)

def display_teacher(request):
    try:
        dis = Teacher_register.objects.filter(subject__course__c_id=request.GET.get("course_id"))
    except Exception:
        data=[]
        data['error_message'] = 'error' 
        return JsonResponse(data)
    return JsonResponse(list(dis.values('tr_id', 'name','subject__subject')), safe = False)

def sign_out(request):
    logout(request)
    request.session.delete()
    return redirect('/home/')

def check_username(request):
    username = request.GET.get("username")
    data = {
    'username_exists': Login.objects.filter(username=username).exists() or User.objects.filter(username=username, is_superuser=True).exists(),
    'error':"This Username already has an account"
    }
    if(data["username_exists"]==False):
        data["success"]="Available"
    return JsonResponse(data)