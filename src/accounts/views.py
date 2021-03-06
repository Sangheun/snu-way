from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignupForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup_form.html", {
        "form": form,
        })

