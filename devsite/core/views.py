from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser  # ✅ Your model


# ⬇️ Replace your current home() view with this one
def home(request):
    """Redirects based on authentication status."""
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return redirect('login')


def custom_404(request, exception=None):
    return render(request, '404.html', status=404)


def signup(request):
    """Handles user signup and redirects to profile page after registration."""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    """User profile page where email can be updated or account deleted."""
    message = None

    if request.method == 'POST':
        if 'update_email' in request.POST:
            new_email = request.POST.get('email')
            if new_email and new_email != request.user.email:
                request.user.email = new_email
                request.user.save()
                message = "Email updated successfully."
        elif 'delete_account' in request.POST:
            request.user.delete()
            return redirect('login')

    return render(request, 'core/profile.html', {'message': message})


# ⬇️ Add this new view at the end of the file
@login_required
def logout_view(request):
    """Logs out the user and redirects to login page."""
    logout(request)
    return redirect('login')