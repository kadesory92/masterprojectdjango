from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),

    path('dashboard/', views.dashboard, name="dashboard"),

    path('create_custom_user/', views.create_custom_user, name='create_custom_user'),
    path('create_student/', views.create_student, name='create_student'),
    path('list_students/', views.list_students, name='list_students'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),

    path('create_teacher/', views.create_teacher, name='create_teacher'),
    path('list_teachers/', views.list_teachers, name='list_teachers'),
    path('update_teacher/<int:teacher_id>/', views.update_teacher, name='update_teacher'),
    path('delete_teacher/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),

    path('create_parent/', views.create_parent, name='create_parent'),
    path('list_parents/', views.list_parents, name='list_parents'),
    path('update_parent/<int:parent_id>/', views.update_parent, name='update_parent'),
    path('delete_parent/<int:parent_id>/', views.delete_parent, name='delete_parent'),

    path('create_study_class/', views.create_study_class, name='create_study_class'),
    path('list_study_classes/', views.list_study_classes, name='list_study_classes'),
    path('update_study_class/<int:class_id>/', views.update_study_class, name='update_study_class'),
    path('delete_study_class/<int:class_id>/', views.delete_study_class, name='delete_study_class'),

    path('create_subject/', views.create_subject, name='create_subject'),
    path('list_subjects/', views.list_subjects, name='list_subjects'),
    path('update_subject/<int:subject_id>/', views.update_subject, name='update_subject'),
    path('delete_subject/<int:subject_id>/', views.delete_subject, name='delete_subject'),

    path('create_course/', views.create_course, name='create_course'),
    path('list_courses/', views.list_courses, name='list_courses'),
    path('update_course/<int:course_id>/', views.update_course, name='update_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),

    path('create_enrollment/', views.create_enrollment, name='create_enrollment'),
    path('list_enrollments/', views.list_enrollments, name='list_enrollments'),
    path('update_enrollment/<int:enrollment_id>/', views.update_enrollment, name='update_enrollment'),
    path('delete_enrollment/<int:enrollment_id>/', views.delete_enrollment, name='delete_enrollment'),

    path('create_attendance/', views.create_attendance, name='create_attendance'),
    path('list_attendance/', views.list_attendance, name='list_attendance'),
    path('update_attendance/<int:attendance_id>/', views.update_attendance, name='update_attendance'),
    path('delete_attendance/<int:attendance_id>/', views.delete_attendance, name='delete_attendance'),

    path('create_classroom/', views.create_classroom, name='create_classroom'),
    path('list_classrooms/', views.list_classrooms, name='list_classrooms'),
    path('update_classroom/<int:classroom_id>/', views.update_classroom, name='update_classroom'),
    path('delete_classroom/<int:classroom_id>/', views.delete_classroom, name='delete_classroom'),

    path('create_exam/', views.create_exam, name='create_exam'),
    path('list_exams/', views.list_exams, name='list_exams'),
    path('update_exam/<int:exam_id>/', views.update_exam, name='update_exam'),
    path('delete_exam/<int:exam_id>/', views.delete_exam, name='delete_exam'),

    path('create_type_exam/', views.create_type_exam, name='create_type_exam'),
    path('list_type_exams/', views.list_type_exams, name='list_type_exams'),
    path('update_type_exam/<int:type_exam_id>/', views.update_type_exam, name='update_type_exam'),
    path('delete_type_exam/<int:type_exam_id>/', views.delete_type_exam, name='delete_type_exam'),

    path('create_take_exam/', views.create_take_exam, name='create_take_exam'),
    path('list_take_exams/', views.list_take_exams, name='list_take_exams'),
    path('update_take_exam/<int:take_exam_id>/', views.update_take_exam, name='update_take_exam'),
    path('delete_take_exam/<int:take_exam_id>/', views.delete_take_exam, name='delete_take_exam'),

    path('create_teaching/', views.create_teaching, name='create_teaching'),
    path('list_teachings/', views.list_teachings, name='list_teachings'),
    path('update_teaching/<int:teaching_id>/', views.update_teaching, name='update_teaching'),
    path('delete_teaching/<int:teaching_id>/', views.delete_teaching, name='delete_teaching'),
]
