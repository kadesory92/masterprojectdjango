from django.contrib.auth.decorators import login_required
from functools import wraps

from django.shortcuts import redirect


def admin_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login if user is not admin

    return wrapped_view


def teacher_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'teacher':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login if user is not teacher

    return wrapped_view


def student_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'student':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login if user is not student

    return wrapped_view


def parent_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'parent':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login if user is not parent

    return wrapped_view
