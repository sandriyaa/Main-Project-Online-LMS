from django.db import models

class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.TextField()
    user_type = models.CharField(max_length=15)
    status = models.BooleanField(default=True)
    class Meta:
        db_table = 'tb_Login'

class Student_register(models.Model):
    sr_id = models.AutoField(primary_key=True)
    login = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    contact_number = models.BigIntegerField()
    address = models.TextField()  
    image = models.TextField(null=True)  
    class Meta:
        db_table = 'tb_Student_register'

class Subject(models.Model):
    s_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=80)
    class Meta:
        db_table = 'tb_Subject'

class Teacher_register(models.Model):
    tr_id = models.AutoField(primary_key=True)
    login = models.ForeignKey(Login,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    contact_number = models.BigIntegerField()
    address = models.TextField()  
    experience = models.CharField(max_length=30)
    qualification = models.CharField(max_length=50)
    image = models.TextField(null=True) 
    class Meta:
        db_table = 'tb_Teacher_register'

class Category(models.Model):
    ct_id = models.AutoField(primary_key=True)
    course_category = models.CharField(max_length=100)
    class Meta:
        db_table = 'tb_Category'

class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    subjects = models.ManyToManyField(Subject)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    course_name = models.CharField(max_length=100) 
    description = models.TextField(null=True)
    fees = models.FloatField()
    image = models.TextField(null=True) 
    certificate_course = models.BooleanField()
    class Meta:
        db_table = 'tb_Course'

class Batch(models.Model):
    b_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    teacher = models.ManyToManyField(Teacher_register)
    title = models.CharField(max_length=150)
    closing_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=False)
    class Meta: 
        db_table = 'tb_Batch'

class Enrollment(models.Model):
    e_id = models.AutoField(primary_key=True)
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE)
    student = models.ForeignKey(Student_register,on_delete=models.CASCADE)
    amount = models.FloatField()
    enrolled_at = models.DateTimeField(auto_now_add=True) 
    class Meta:
        db_table='tb_Enrollment'

class Lesson(models.Model):
    l_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True)
    teacher = models.ForeignKey(Teacher_register,on_delete=models.SET_NULL,null=True,related_name="lessons")
    title = models.CharField(max_length=50)
    video = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'tb_Lesson'

class Lecture_notes(models.Model):
    ln_id = models.AutoField(primary_key=True)
    video = models.ForeignKey(Lesson,on_delete=models.SET_NULL,null=True)
    note = models.TextField()
    class Meta:
        db_table = 'tb_Lecture_notes'

class Doubts(models.Model):
    d_id = models.AutoField(primary_key=True)
    sender =  models.ForeignKey(Login,on_delete=models.CASCADE,null=True,related_name='sender')
    receiver =  models.ForeignKey(Login,on_delete=models.CASCADE,null=True,related_name='receiver')
    msg = models.TextField(blank=True)
    msg_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    class Meta:
        db_table='tb_Doubts'

class Exam(models.Model):
    e_id = models.AutoField(primary_key=True)
    batch = models.ManyToManyField(Batch)
    teacher = models.ForeignKey(Teacher_register,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)  
    topic = models.TextField(null=True)
    duration = models.FloatField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'tb_Exam'

class Questions(models.Model):
    q_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam,on_delete=models.SET_NULL,null=True)
    question = models.TextField()
    optionA = models.CharField(max_length=200)
    optionB = models.CharField(max_length=200)
    optionC = models.CharField(max_length=200)
    optionD = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    class Meta:
        db_table = 'tb_Questions'

class Answers(models.Model):
    a_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student_register,on_delete=models.SET_NULL,null=True)
    question = models.ForeignKey(Questions,on_delete=models.SET_NULL,null=True)
    answer = models.CharField(max_length=200,null=True)
    class Meta:
        db_table = 'tb_Answers'

class Assignment(models.Model):
    a_id = models.AutoField(primary_key=True)
    batch = models.ManyToManyField(Batch)
    teacher = models.ForeignKey(Teacher_register,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_mark = models.FloatField()
    status = models.BooleanField(default=False)
    class Meta:
        db_table = 'tb_Assignment'

class Submission(models.Model):
    s_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student_register,on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.SET_NULL, null=True)
    submitted_date = models.DateField(auto_now_add=True)
    assignment_file = models.TextField()
    mark = models.FloatField(null=True)
    class Meta:
        db_table = 'tb_Submission'

class Feedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student_register,on_delete=models.CASCADE)
    feedback_date = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField()
    class Meta:
        db_table = 'tb_Feedback'