from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserRegistrationForm, ProfileImageForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegister(View):
    def get(self, request):
        form = UserRegistrationForm
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'You registered successfully!', 'success')
            return redirect('core:home')
        return render(request, 'accounts/register.html', {'form': form})  # if form isn't valid, load the form with error messages


class Login(auth_views.LoginView):
    template_name = 'accounts/login.html'


class Profile(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'
    form_class = ProfileImageForm

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        return render(request, self.template_name, {'user': user, 'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your image was uploaded successfully!', 'success')
            return redirect('accounts:profile', request.user.username)







