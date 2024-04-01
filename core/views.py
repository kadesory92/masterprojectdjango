from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserForm, StudentForm, TeacherForm, ParentForm, StudyClassForm, SubjectForm, CourseForm, \
    EnrollmentForm, AttendanceForm, ClassroomForm, ExamForm, TypeExamForm, TakeExamForm, TeachingForm
from .models import Student, Teacher, Parent, StudyClass, Subject, Course, Enrollment, Attendance, \
    Classroom, Exam, TypeExam, TakeExam, Teaching


def home(request):
    return render(request, 'home.html')


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


# View for creating a new custom user
def create_custom_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = CustomUserForm()
    return render(request, 'custom_user_form.html', {'form': form})


def create_user(request, role):
    global entity_form
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        if role == 'student':
            entity_form = StudentForm(request.POST, request.FILES)
        elif role == 'teacher':
            entity_form = TeacherForm(request.POST, request.FILES)
        elif role == 'parent':
            entity_form = ParentForm(request.POST, request.FILES)

        if user_form.is_valid() and entity_form.is_valid():
            user = user_form.save()
            entity = entity_form.save(commit=False)
            entity.user = user
            entity.save()

            # Envoi de notification par téléphone
            # send_notification(user)

            return redirect('success_url')  # Redirige vers une page de succès
    else:
        user_form = CustomUserForm()
        if role == 'student':
            entity_form = StudentForm()
        elif role == 'teacher':
            entity_form = TeacherForm()
        elif role == 'parent':
            entity_form = ParentForm()

    return render(request, 'user_form.html', {'user_form': user_form, 'entity_form': entity_form, 'role': role})


# def send_notification(user):
#     # Configurez votre compte Twilio
#     TWILIO_ACCOUNT_SID = settings.TWILIO_ACCOUNT_SID
#     TWILIO_AUTH_TOKEN = settings.TWILIO_AUTH_TOKEN
#     TWILIO_PHONE_NUMBER = settings.TWILIO_PHONE_NUMBER
#
#     message = f"Votre compte a été créé avec succès. Votre nom d'utilisateur est {user.username}."
#     phone_number = user.phone_number
#     if phone_number:
#         try:
#             # Envoyer une notification par SMS
#             client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#             message = client.messages.create(
#                 body=message,
#                 from_=TWILIO_PHONE_NUMBER,
#                 to=phone_number
#             )
#         except Exception as e:
#             # Manage sending errors de SMS
#             print("Error when sending SMS :", e)


# View for creating a new student
# def create_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('success_url')  # Redirect to a success page
#     else:
#         form = StudentForm()
#     return render(request, 'student_form.html', {'form': form})


def create_student(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        student_form = StudentForm(request.POST, request.FILES)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()

            # Envoi de notification par téléphone
            # send_notification(user)

            return redirect('success_url')  # Redirige vers une page de succès
    else:
        user_form = CustomUserForm()
        student_form = StudentForm()
    return render(request, '/admin/student/student_form.html', {'user_form': user_form, 'student_form': student_form})


def list_students(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


# Example view for updating a student
def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})


# Example view for deleting a student
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'student_confirm_delete.html', {'student': student})


# View for creating a new teacher
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = TeacherForm()
    return render(request, 'teacher_form.html', {'form': form})


# View for reading a list of teachers
def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})


# View for updating a teacher
def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teacher_form.html', {'form': form})


# View for deleting a teacher
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'teacher_confirm_delete.html', {'teacher': teacher})


# View for creating a new parent
def create_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = ParentForm()
    return render(request, 'parent_form.html', {'form': form})


# View for reading a list of parents
def list_parents(request):
    parents = Parent.objects.all()
    return render(request, 'parent_list.html', {'parents': parents})


# View for updating a parent
def update_parent(request, parent_id):
    parent = get_object_or_404(Parent, pk=parent_id)
    if request.method == 'POST':
        form = ParentForm(request.POST, request.FILES, instance=parent)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = ParentForm(instance=parent)
    return render(request, 'parent_form.html', {'form': form})


# View for deleting a parent
def delete_parent(request, parent_id):
    parent = get_object_or_404(Parent, pk=parent_id)
    if request.method == 'POST':
        parent.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'parent_confirm_delete.html', {'parent': parent})


# View for creating a new study class
def create_study_class(request):
    if request.method == 'POST':
        form = StudyClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = StudyClassForm()
    return render(request, 'studyclass_form.html', {'form': form})


# View for reading a list of study classes
def list_study_classes(request):
    study_classes = StudyClass.objects.all()
    return render(request, 'studyclass_list.html', {'study_classes': study_classes})


# View for updating a study class
def update_study_class(request, class_id):
    study_class = get_object_or_404(StudyClass, pk=class_id)
    if request.method == 'POST':
        form = StudyClassForm(request.POST, instance=study_class)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = StudyClassForm(instance=study_class)
    return render(request, 'studyclass_form.html', {'form': form})


# View for deleting a study class
def delete_study_class(request, class_id):
    study_class = get_object_or_404(StudyClass, pk=class_id)
    if request.method == 'POST':
        study_class.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'studyclass_confirm_delete.html', {'study_class': study_class})


# View for creating a new subject
def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = SubjectForm()
    return render(request, 'subject_form.html', {'form': form})


# View for reading a list of subjects
def list_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})


# View for updating a subject
def update_subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'subject_form.html', {'form': form})


# View for deleting a subject
def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == 'POST':
        subject.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'subject_confirm_delete.html', {'subject': subject})


# View for creating a new course
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})


# View for reading a list of courses
def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


# View for updating a course
def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})


# View for deleting a course
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'course_confirm_delete.html', {'course': course})


# View for creating a new enrollment
def create_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = EnrollmentForm()
    return render(request, 'enrollment_form.html', {'form': form})


# View for reading a list of enrollments
def list_enrollments(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment_list.html', {'enrollments': enrollments})


# View for updating an enrollment
def update_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, pk=enrollment_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, 'enrollment_form.html', {'form': form})


# View for deleting an enrollment
def delete_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, pk=enrollment_id)
    if request.method == 'POST':
        enrollment.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'enrollment_confirm_delete.html', {'enrollment': enrollment})


# View for creating a new attendance
def create_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = AttendanceForm()
    return render(request, 'attendance_form.html', {'form': form})


# View for reading a list of attendance records
def list_attendance(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendances': attendances})


# View for updating an attendance record
def update_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'attendance_form.html', {'form': form})


# View for deleting an attendance record
def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    if request.method == 'POST':
        attendance.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'attendance_confirm_delete.html', {'attendance': attendance})


# View for creating a new classroom
def create_classroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = ClassroomForm()
    return render(request, 'classroom_form.html', {'form': form})


# View for reading a list of classrooms
def list_classrooms(request):
    classrooms = Classroom.objects.all()
    return render(request, 'classroom_list.html', {'classrooms': classrooms})


# View for updating a classroom
def update_classroom(request, classroom_id):
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = ClassroomForm(instance=classroom)
    return render(request, 'classroom_form.html', {'form': form})


# View for deleting a classroom
def delete_classroom(request, classroom_id):
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    if request.method == 'POST':
        classroom.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'classroom_confirm_delete.html', {'classroom': classroom})


# View for creating a new exam
def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = ExamForm()
    return render(request, 'exam_form.html', {'form': form})


# View for reading a list of exams
def list_exams(request):
    exams = Exam.objects.all()
    return render(request, 'exam_list.html', {'exams': exams})


# View for updating an exam
def update_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = ExamForm(instance=exam)
    return render(request, 'exam_form.html', {'form': form})


# View for deleting an exam
def delete_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    if request.method == 'POST':
        exam.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'exam_confirm_delete.html', {'exam': exam})


# View for creating a new type of exam
def create_type_exam(request):
    if request.method == 'POST':
        form = TypeExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = TypeExamForm()
    return render(request, 'typeexam_form.html', {'form': form})


# View for reading a list of exam types
def list_type_exams(request):
    type_exams = TypeExam.objects.all()
    return render(request, 'typeexam_list.html', {'type_exams': type_exams})


# View for updating an exam type
def update_type_exam(request, type_exam_id):
    type_exam = get_object_or_404(TypeExam, pk=type_exam_id)
    if request.method == 'POST':
        form = TypeExamForm(request.POST, instance=type_exam)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = TypeExamForm(instance=type_exam)
    return render(request, 'typeexam_form.html', {'form': form})


# View for deleting an exam type
def delete_type_exam(request, type_exam_id):
    type_exam = get_object_or_404(TypeExam, pk=type_exam_id)
    if request.method == 'POST':
        type_exam.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'typeexam_confirm_delete.html', {'type_exam': type_exam})


# View for creating a new take exam instance
def create_take_exam(request):
    if request.method == 'POST':
        form = TakeExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = TakeExamForm()
    return render(request, 'takeexam_form.html', {'form': form})


# View for reading a list of take exam instances
def list_take_exams(request):
    take_exams = TakeExam.objects.all()
    return render(request, 'takeexam_list.html', {'take_exams': take_exams})


# View for updating a take exam instance
def update_take_exam(request, take_exam_id):
    take_exam = get_object_or_404(TakeExam, pk=take_exam_id)
    if request.method == 'POST':
        form = TakeExamForm(request.POST, instance=take_exam)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = TakeExamForm(instance=take_exam)
    return render(request, 'takeexam_form.html', {'form': form})


# View for deleting a take exam instance
def delete_take_exam(request, take_exam_id):
    take_exam = get_object_or_404(TakeExam, pk=take_exam_id)
    if request.method == 'POST':
        take_exam.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'takeexam_confirm_delete.html', {'take_exam': take_exam})


# View for creating a new teaching instance
def create_teaching(request):
    if request.method == 'POST':
        form = TeachingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = TeachingForm()
    return render(request, 'teaching_form.html', {'form': form})


# View for reading a list of teaching instances
def list_teachings(request):
    teachings = Teaching.objects.all()
    return render(request, 'teaching_list.html', {'teachings': teachings})


# View for updating a teaching instance
def update_teaching(request, teaching_id):
    teaching = get_object_or_404(Teaching, pk=teaching_id)
    if request.method == 'POST':
        form = TeachingForm(request.POST, instance=teaching)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = TeachingForm(instance=teaching)
    return render(request, 'teaching_form.html', {'form': form})


# View for deleting a teaching instance
def delete_teaching(request, teaching_id):
    teaching = get_object_or_404(Teaching, pk=teaching_id)
    if request.method == 'POST':
        teaching.delete()
        return redirect('success_url')  # Redirect to a success page
    return render(request, 'teaching_confirm_delete.html', {'teaching': teaching})
