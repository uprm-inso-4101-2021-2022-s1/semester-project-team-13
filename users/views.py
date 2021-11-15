from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from userProfile import views as userProfileView
from beach.models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usernameInstance = form.cleaned_data.get('username')
            userInstance = get_object_or_404(User, username = usernameInstance)
            profile = Profile(img = 'default_user_pic.jpg',user = userInstance, bio = "I love beaches!")
            profile.save()
            messages.success(request, f'Your account has been created! You are now able to log in {usernameInstance}!')
            return redirect('login')
    else: #get request
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, userProfileView.userProfile)