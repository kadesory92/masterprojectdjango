from functools import wraps
from django.shortcuts import redirect


def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == role:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')  # Redirect to login if user doesn't have the required role

        return wrapped_view

    return decorator
