from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from blog.models import Blog
# Create your views here.

def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('blog:home')
    form = RegisterForm()
    dict = {'form': form}
    return render(request, 'User/register.html', context=dict)


def UserLoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('blog:home')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    dict = {'form': form}
    return render(request, 'User/login.html', context=dict)

def LogoutView(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('blog:home')

@login_required
def ProfileFormView(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('user:profile')
    form=ProfileForm()
    dict= {'form': form}
    return render(request, 'User/user_main_profile.html', context=dict)

@login_required
def UserProfileView(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except:
        #form = ProfileForm()
        return redirect('user:profile-form')
    
    blog_list = Blog.objects.filter(user=user)
    # print(blog_list)
    dict = {'data':user_profile, 'blog_list':blog_list}
    return render(request, 'User/profile.html', context=dict)





