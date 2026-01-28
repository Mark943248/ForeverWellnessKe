from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Pages.views import home


# user registration view
def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # saves users info on database
            form.save()
            username = form.cleaned_data.get('username') # get username
            password = form.cleaned_data.get('password1') # get password
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            # success message
            messages.success(request, f'{username}, your account has been created successfully!')
            # redirect to home page
            return redirect(home)
        else:
            # error message
            messages.error(request, 'Please correct the errors.')
    return render(request, 'users/register.html', {'form': form})

# user login view
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username') # get username
        password = request.POST.get('password') # get password
        # checks if username and password exist
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Login successful. Welcome back, {username}!')
            return redirect('user_dashboard')  # redirect to user dashboard
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'users/login_user.html')

# users dashboard view
@login_required(login_url='login')
def user_dashboard(request):
    name = request.user.username # get logged in user's username
    return render(request, 'users/dashboard.html', {'name': name})

# user logout view
def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect(home)