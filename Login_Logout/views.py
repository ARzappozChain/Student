from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from .models import User, Sponsor, Profile
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from .utils import generate_refferal_link

User = get_user_model()



# এখানে আমি একজন ইউজার রেজিস্টার করার জন্য ভিউস এর কোড করসি 

def Register(request):
    ref_code = request.GET.get('ref_code')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            if ref_code:
                
                try:
                    sponsor =Sponsor.objects.get(code = ref_code)
                    user.sponsor.recommended_by = sponsor.user
                    
                    user.save()
                    
                except Sponsor.DoesNotExist:
                    pass
            
            messages.success(request, 'Account registered successfully')
            return redirect('Registerpage')
        
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form':form})


# এখানে আমি একজন ইউজার login করার জন্য ভিউস এর কোড করসি

def LoginView(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(email = email, password = password)
            
            if user is not None:
                login(request,user)
                messages.success(request, f' welcome {user.first_name} {user.last_name} !!')
                return redirect('homepage')
            
            else:
                messages.success(request,'Loggin info incorrect')
                
    else:
        form = AuthenticationForm()
        
    return render(request,'login.html', {'form':form} )


# এখানে আমি একজন ইউজার Logout করার জন্য ভিউস এর কোড করসি


@login_required
def LogoutView(request):
    user = request.user
    logout(request)
    messages.success(request, f'{user.first_name} {user.last_name} is successfully logged out.')
    return redirect('homepage')

