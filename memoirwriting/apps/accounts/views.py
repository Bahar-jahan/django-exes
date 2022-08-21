from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.views import View
from .forms import *
from .models import *

# ==================================================================


class RegisterUserView(View):
    def dispatch(self, request,  *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("main:index")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = RegisterUserForm()
        return render(request, 'accounts_app/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            CustomUser.objects.create_user(
                email=user['email'],
                name=user['name'],
                family=user['family'],
                mobile_number=user['mobile_number'],
                gender=user['gender'],
                password=user['password']

            )
            messages.success(request, 'ثبت نام با موفقیت انجام شد ', 'success')
            return redirect('main:index')
        else:
            messages.error(request, 'ثبت نام با موفقیت انجام نشد ', 'error')
            return render(request, 'accounts_app/register.html', {'form': form})


# ==================================================================
class LoginUserView(View):
    def dispatch(self, request,  *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("main:index")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = LoginUserForms()
        context = {'form': form}
        return render(request, 'accounts_app/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginUserForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd.get('email'),
                                password=cd.get('password'))
            if user is not None:
                db_user = CustomUser.objects.get(email=user.email)
                if not db_user.is_admin:
                    messages.success(
                        request, 'ورود با موفقیت انجام شد ', 'success')
                    login(request, user)
                    return redirect('main:index')
                else:
                    messages.error(
                        request, 'کاربر ادمین نمیتواند ازین قسمت وارد شود ', 'danger')
                    return render(request, 'accounts_app/login.html', {'form': form})
        else:
            messages.error(request, ' اطلاعات وارده معتبر نمیباشد ', 'error')
            return render(request, 'accounts_app/login.html', {'form': form})


# ==================================================================
class LogoutUserView(View):
    def dispatch(self, request,  *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("main:index")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'خدا نگهدار', 'success')
        return redirect('main:index')


# ==================================================================
class ProfileUserView(View):
    def dispatch(self, request,  *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("main:index")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        if user.gender==True: 
            ge="مرد "
        else:
            ge="زن"    
        context = {'email': user.email,
                   'name': user.name,
                   'family': user.family,
                   'mobile_number': user.mobile_number,
                   'gender': ge,
                   }          
        return render(request , 'accounts_app/profile.html',context)               


# ==================================================================
class EditProfileUserView(View):
    def dispatch(self, request,  *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("main:index")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form=EditUserForm()
        context = {
                'form':form
                   }          
        return render(request , 'accounts_app/editProfile.html',context)              

    def put(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        form=EditUserForm(request.POST)
        if form.is_valid():
            current_user =form.cleaned_data
            print(current_user)
            user.name=current_user['name']
            user.save()
            return redirect('accounts:profile')   



