from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from profiles.form import AddressForm, ProfileForm
from profiles.models import CustomerAddress 
from account.models import CustomUser

@method_decorator(login_required(login_url='account:login'), name='dispatch')
class CustomerProfileView(View):
    
    def get(self, request):
        form = AddressForm
        user = CustomUser.objects.get(username = request.user.username)
        profiles_form = ProfileForm(instance= user)
        addresses = CustomerAddress.objects.filter(user = request.user).order_by('-default')
        context = {
            'addresses' : addresses,
            'form' : form,
            'profiles_form' : profiles_form
        }
        return render(request, 'user/profile.html', context)
    def post(self, request):
        profile_form = ProfileForm( request.POST, request.FILES, instance= request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile edited successfuly')
            return redirect('profiles:customer_profile')
        messages.error(request, 'Invalid data')
        return redirect('profiles:coustomer_profile')

@method_decorator(login_required(login_url='account:login'), name='dispatch')
class AdminProfileView(View):
    def get(self, request):
        profile_form = ProfileForm(instance= request.user)
        context = {
            'profile_form' : profile_form
        }
        return render(request, 'super_admin/profile.html', context)

    def post(self, request):
        user_profile_form = ProfileForm( request.POST, request.FILES, instance= request.user)
        if user_profile_form.is_valid():
            user_profile_form.save()
            messages.success(request, 'Profile edited successfuly')
            return redirect('profiles:admin_profile')
        messages.error(request, 'Invalid data')
        return redirect('profiles:admin_profile')



@login_required(login_url='account:login')
def addressView(request):

    if request.method == 'POST':
        default_address = CustomerAddress.objects.filter(user = request.user, default = True)
        for address in default_address:
            address.default = False
            address.save()
        name = request.POST.get('name')
        address = request.POST.get('address')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        mob = request.POST.get('mob')

        try:
            edit_address = CustomerAddress.objects.get(edit = True)
            edit_address.name = name
            edit_address.address = address
            edit_address.state = state
            edit_address.pin = pin
            edit_address.mob = mob
            edit_address.edit = False
            edit_address.default = True
            edit_address.save()

            print('update')
        except:
            CustomerAddress.objects.create(
            user = request.user, 
            name = name, 
            address = address, 
            state = state, 
            pin = pin, 
            mob = mob, 
            default = True
            )
            data = { 
                'status' : 'Product added successfully'
            }
            print('create')
            return JsonResponse(data)
    
    form = AddressForm
    context = {'form' : form }
    return render(request, 'user/profile.html', context)

@login_required(login_url='account:login')
def addressDefaultView(request):
    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        all_address = CustomerAddress.objects.filter(user = request.user)
        for address in all_address:
            address.default = False
            address.save()
        address = CustomerAddress.objects.get(user = request.user, id = address_id)
        address.default = True
        address.save()
        data = { 
            'status' : 'set to default'
        }
        return JsonResponse(data)

@login_required(login_url='account:login')
def addressDeleteView(request):
    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        address = CustomerAddress.objects.get(user = request.user, id = address_id)
        address.delete()
        data = { 
            'status' : 'Product added successfully'
        }
        return JsonResponse(data)


@login_required(login_url='account:login')
def addressEdit(request):
    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        address = CustomerAddress.objects.get(user = request.user, id = address_id)
        address.edit = True
        address.save()
        data = {
            'name' : address.name,
            'address' : address.address,
            'state' : address.state,
            'pin' : address.pin,
            'mob' : address.mob
        }
        return JsonResponse(data)
