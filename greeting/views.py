from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout  # Import logout from django.contrib.auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# View for handling user login
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Create an AuthenticationForm instance with data from POST request
        if form.is_valid():  # Check if the form is valid
            user = form.get_user()  # Retrieve the authenticated user
            login(request, user)  # Log in the user
            return redirect('createproduct')  # Redirect to a page after successful login
    else:
        form = AuthenticationForm()  # Create an empty AuthenticationForm instance

    return render(request, 'login.html', {'form': form})  # Render the login page with the form


# View for handling user signup
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Create a UserCreationForm instance with data from POST request
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the new user
            return redirect('createproduct')  # Redirect to a page after successful signup
    else:
        form = UserCreationForm()  # Create an empty UserCreationForm instance

    return render(request, 'signup.html', {'form': form})  # Render the signup page with the form


# View for logging out users
@login_required(login_url='/login')  # Decorator to ensure only authenticated users can access this view
def logout_view(request):
    if request.method == 'POST':
        logout(request)  # Log out the user
        return redirect('home')  # Redirect to the home page after logout

    return render(request, 'logout.html', {'user': request.user})  # Render the logout page with the current user


@login_required(login_url='/login')
def aboutUs(request):
    return render(request, 'about-us.html')  # Render the about us page
