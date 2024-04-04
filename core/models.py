from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'ADMIN'),
        ('teacher', 'TEACHER'),
        ('student', 'STUDENT'),
        ('parent', 'PARENT'),
    ]

    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, default='M')

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    address = models.TextField(max_length=200, null=True)
    phone_number = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=150, null=True, unique=True)

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"


class Student(models.Model):
    objects = None
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.date_of_birth}"


class Teacher(models.Model):
    objects = None
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.date_of_birth}"


class Parent(models.Model):
    objects = None
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='parent_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.date_of_birth}"


class Parenting(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)


class StudyClass(models.Model):
    objects = None
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)


class Subject(models.Model):
    objects = None
    subject_name = models.CharField(max_length=100)


class Course(models.Model):
    objects = None
    class_id = models.ForeignKey(StudyClass, on_delete=models.CASCADE, null=True)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    classroom_id = models.ForeignKey('Classroom', on_delete=models.CASCADE, null=True)


class Enrollment(models.Model):
    objects = None
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    class_id = models.ForeignKey(StudyClass, on_delete=models.CASCADE, null=True)
    enrollment_date = models.DateField()


class Attendance(models.Model):
    objects = None
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, null=True)
    attendance_date = models.DateField()
    # status = models.CharField(max_length=10)
    status_choices = (
        ('present', 'Present'),
        ('absent', 'Absent')
    )
    status = models.CharField(max_length=10, choices=status_choices, default='present')


class Classroom(models.Model):
    objects = None
    capacity = models.IntegerField()


class Exam(models.Model):
    objects = None
    date_exam = models.DateField()
    coefficient = models.IntegerField()
    type_exam = models.ForeignKey('TypeExam', on_delete=models.CASCADE, null=True)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)


class TypeExam(models.Model):
    objects = None
    designation = models.CharField(max_length=50)


class TakeExam(models.Model):
    objects = None
    mark = models.DecimalField(max_digits=5, decimal_places=2)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)


class Teaching(models.Model):
    objects = None
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
