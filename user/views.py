from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to a specific URL after login (change 'home' to your desired URL)
        else:
            # Authentication failed
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        # Display the login form
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to a specific URL after logout (change 'home' to your desired URL)
