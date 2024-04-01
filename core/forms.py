from django import forms
from .models import CustomUser, Student, Teacher, Parent, StudyClass, Subject, Course, Enrollment, Attendance, \
    Classroom, Exam, TypeExam, TakeExam, Teaching


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'gender', 'role', 'first_name', 'last_name', 'address', 'phone_number',
                  'email']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'date_of_birth', 'photo']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'date_of_birth', 'photo']


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['user', 'date_of_birth', 'photo']


class StudyClassForm(forms.ModelForm):
    class Meta:
        model = StudyClass
        fields = ['class_name', 'section']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['class_id', 'subject_id', 'teacher_id', 'classroom_id']


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student_id', 'class_id', 'enrollment_date']


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['enrollment', 'attendance_date', 'status']


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['capacity']


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['date_exam', 'coefficient', 'type_exam', 'subject_id']


class TypeExamForm(forms.ModelForm):
    class Meta:
        model = TypeExam
        fields = ['designation']


class TakeExamForm(forms.ModelForm):
    class Meta:
        model = TakeExam
        fields = ['mark', 'exam_id', 'student_id']


class TeachingForm(forms.ModelForm):
    class Meta:
        model = Teaching
        fields = ['teacher_id', 'subject_id']
