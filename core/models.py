from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'ADMIN'),
        ('teacher', 'TEACHER'),
        ('student', 'STUDENT'),
        ('parent', 'PARENT'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    # gender = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=gender_choices, default='M')


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    # gender = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=gender_choices, default='M')


class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='parent_photos/', blank=True, null=True)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=gender_choices, default='M')


class Parenting(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)


class StudyClass(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Course(models.Model):
    class_field = models.ForeignKey(StudyClass, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_field = models.ForeignKey(StudyClass, on_delete=models.CASCADE)
    enrollment_date = models.DateField()


class Grade(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    exam_date = models.DateField()
    marks = models.DecimalField(max_digits=5, decimal_places=2)


class Attendance(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    # status = models.CharField(max_length=10)
    status_choices = (
        ('present', 'Present'),
        ('absent', 'Absent')
    )
    status = models.CharField(max_length=10, choices=status_choices, default='present')
