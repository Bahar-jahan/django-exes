from cProfile import label
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

#----------------------------------------------------------------
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('email', 'name','family','mobile_number','gender')

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

#----------------------------------------------------------------

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="برای تغییر رمز باید <a href='../password'>اینجا</a> کلیلک کنید")
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'name','family','mobile_number','gender', 'is_active', 'is_admin')

#----------------------------------------------------------------
CHOICE_GENDER=((True,"مرد"),(False,"زن"))
class RegisterUserForm(forms.Form):
    email= forms.EmailField(label="",error_messages={'required':'این فیلد نمیتواند خالی باشد ' }, widget=forms.TextInput( attrs={'class' :'form-control' ,'placeholder':'ایمیل'}))
    name= forms.CharField(label="", widget=forms.TextInput(attrs={'class' :'form-control' ,'placeholder':'نام '}))
    family =forms.CharField(label="", widget=forms.TextInput(attrs={'class' :'form-control' ,'placeholder':'نام خانوادگی'}))
    mobile_number=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'شماره موبایل '}) )
    gender= forms.ChoiceField(label="",choices=CHOICE_GENDER , )
    password= forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'پسورد'}))
    repped_password= forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'تکرار پسورد '}))

# -------------------------------------------------------------------------------
class LoginUserForms(forms.Form):
    email= forms.EmailField( label="",error_messages={'required':'این فیلد نمیتواند خالی باشد ' }, widget=forms.TextInput( attrs={'class' :'form-control' ,'placeholder':'ایمیل'}))
    password= forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'پسورد'}))



# -----------------------------------------------------------------------------------
class EditUserForm(forms.Form):
    name= forms.CharField(label="",widget=forms.TextInput(attrs={'class' :'form-control' ,'placeholder':'نام '}))
    family =forms.CharField(label="", widget=forms.TextInput(attrs={'class' :'form-control' ,'placeholder':'نام خانوادگی'}))
    mobile_number=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'شماره موبایل '}) )
    gender= forms.ChoiceField(label="",choices=CHOICE_GENDER , )
    password= forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'پسورد'}))
    repped_password= forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'تکرار پسورد '}))





# class LoginForm(forms.Form):
#     email = forms.EmailField(label="",error_messages={"required":'ایمیل نمی تواند خالی باشد'},)
#     password = forms.CharField(label="",error_messages={"required":'رمز عبور نمی تواند خالی باشد'}
#                                , widget=forms.PasswordInput())
    
    