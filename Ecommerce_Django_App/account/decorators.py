from django.http import HttpResponseNotAllowed
from django.contrib import messages
from django.shortcuts import redirect
from .models import CustomUser


# ============== admin login decorator ============

def admin_login_required(fn):


    def wrapper(request=None, *args, **kwargs):
            if request.user.is_authenticated:
                user = CustomUser.objects.get(email = request.user)

                if user.is_admin:
                    return fn(request, *args, **kwargs)
                else:
                    messages.info(request, 'Login required, make sure you are an admin or staff')
                    return redirect('account:admin_login')
            messages.info(request, 'Login required, make sure you are an admin or staff')
            return redirect('account:admin_login')
    return wrapper