# from .forms import CustomSignupForm
# # from .forms import CustomUserCreationForm as UserCreationForm
# # from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
# from django.contrib.auth import login

# def home(request):
#     return render(request, 'home.html')

# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomSignupForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomSignupForm()
    return render(request, 'registration/signup.html', {'form': form})


