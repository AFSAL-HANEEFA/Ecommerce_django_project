from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth import logout

from account.forms import CustomUserCreationForm
from account.twilio import get_otp, check_otp


# ============== mobile number verification =============

def send_otp(request):
    
    if request.method == 'POST':
        mob_number = request.POST.get('mobile')
        request.session['mob_number'] = mob_number
        if(get_otp(request, mob_number)):
            return redirect('account:verify_otp')
    return render(request, 'user/send_otp.html')

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if(check_otp(request, otp, mob_number = request.session['mob_number'])):
            messages.success(request, 'Mobile verification successfuly completed!')
            return redirect('account:create_account')
        else:
            messages.error(request, 'Invalid OTP! Please enter valid OTP')
        
    return render(request, 'user/verify_otp.html')

# ================== user authentication =================

def userCreationView(request):
    try:
        mob_number = request.session['mob_number']
    except:

        messages.info(request, 'Session expired, Please try again..')
        return redirect('account:send_otp')
    if mob_number:
        form = CustomUserCreationForm
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                if form.cleaned_data.get('mobile') == mob_number:
                    form.save()
                    messages.success(request, 'Registered successfully! Login to Continue...')
                    return redirect('account:login')
                else:
                    messages.error(request, 'Mobile number is not verfied')
            context = { 'form' : form, 'mobile' : mob_number}
            return render(request, 'user/user_creation.html', context)
        context = { 'form' : form, 'mobile' : mob_number}
        return render(request, 'user/user_creation.html', context)



def logoutView(request):
    logout(request)
    return redirect('home')


class AdminCreationView(View):
    def get(self, request):
        form = CustomUserCreationForm
        return render(request, 'super_admin/user_creation.html', {'form' : form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Please login to continue')
            return redirect('account:admin_login')
        messages.error(request, 'Invalid input')
        return render(request, 'super_admin/user_creation.html', {'form' : form})


def adminLogoutView(request):
    logout(request)
    messages.success(request, 'Logged out!')
    return redirect('account:admin_login')