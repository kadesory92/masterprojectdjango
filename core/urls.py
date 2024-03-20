from django.urls import path

from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
        path('student/<int:student_id>/edit', views.edit_student, name='edit_student'),
        path('student/<int:student_id>/delete', views.delete_student, name='delete_student'),
]
