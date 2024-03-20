from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import render

from core.forms import StudentForm
from core.models import Attendance, Teacher, Student


def dashboard(request):
    # Retrieve the role of the currently logged-in user
    user_role = request.user.role

    # Define the default context
    context = {'dashboard_content': 'Bienvenue!'}

    # Depending on the role, customize the dashboard content and template
    if user_role == 'admin':
        # Administrator-specific logic and template
        template_name = 'admin_dashboard.html'
        context['dashboard_content'] = 'Welcome, administrator!'
    elif user_role == 'student':
        # Student-specific logic and template
        template_name = 'student_dashboard.html'
        context['dashboard_content'] = 'Welcome, student!'
    elif user_role == 'teacher':
        # Teacher-specific logic and template
        template_name = 'teacher_dashboard.html'
        context['dashboard_content'] = 'Welcome, teacher!'
    elif user_role == 'parent':
        # Parent-specific logic and template
        template_name = 'parent_dashboard.html'
        context['dashboard_content'] = 'Bienvenue, parent!'
    else:
        # Default logic and template
        template_name = 'default_dashboard.html'

    # Render the appropriate template with the context
    return render(request, template_name, context)


def home(request):
    return render(request, 'home.html')


def admin_dashboard(request):
    # Total number of students and teachers
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()

    # Percentage of students' attendance and absence
    total_attendance = Attendance.objects.count()
    total_present = Attendance.objects.filter(status='present').count()
    total_absent = Attendance.objects.filter(status='absent').count()
    if total_attendance > 0:
        percentage_present = (total_present / total_attendance) * 100
        percentage_absent = (total_absent / total_attendance) * 100
    else:
        percentage_present = 0
        percentage_absent = 0

    students_list = Student.objects.all()
    paginator = Paginator(students_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'percentage_present': percentage_present,
        'percentage_absent': percentage_absent,
        'page_obj': page_obj
    }
    return render(request, 'admin/admin_dashboard.html', context)


def edit_student(request):
    render(request, 'admin/edit_student.html')


def delete_student(request):
    render(request, 'admin/delete_student.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

# Créez des vues similaires pour les autres modèles (Teacher, Parent, Class, Subject, Course, Enrollment, Grade, Attendance)
